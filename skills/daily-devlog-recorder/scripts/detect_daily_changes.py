#!/usr/bin/env python3
"""
detect_daily_changes.py - Multi-Layer Daily Change Detection Engine for daily-devlog-recorder
Detects file system modifications, Git uncommitted changes, and Git commits for a given date.
Works reliably even when Git commits are infrequent or absent.
"""

import os
import sys
import argparse
import datetime
import json
import subprocess
from pathlib import Path

DEFAULT_IGNORE_DIRS = {
    '.git', 'node_modules', 'vendor', 'backups', 'tmp', 'temp', 
    '__pycache__', '.antigravity', '.gemini', 'brain', 'dist', 
    'build', '.vscode', '.idea', '.scratch', 'scratch'
}

DEFAULT_IGNORE_FILES = {
    'timing.json', 'grading.json', 'feedback.json', 'benchmark.json'
}

def run_cmd(cmd, cwd='.'):
    """Run shell command safely and return stdout, or empty string on failure."""
    try:
        res = subprocess.run(
            cmd, cwd=cwd, shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
            text=True, encoding='utf-8', errors='replace'
        )
        if res.returncode == 0:
            return res.stdout.strip()
    except Exception:
        pass
    return ""

def get_git_info(target_dir, target_date_str):
    """Extract Git status, uncommitted diffs, and commits for the target date."""
    git_dir = os.path.join(target_dir, '.git')
    is_git = os.path.exists(git_dir)
    
    info = {
        'is_git_repo': is_git,
        'current_branch': '',
        'commits_today': [],
        'uncommitted_files': [],
        'git_diff_stat': '',
        'total_insertions': 0,
        'total_deletions': 0
    }
    
    if not is_git:
        return info

    info['current_branch'] = run_cmd('git rev-parse --abbrev-ref HEAD', cwd=target_dir) or 'unknown'
    
    # Git commits on target date
    # Format: hash|author|iso_date|subject
    git_log_raw = run_cmd(
        f'git log --since="{target_date_str} 00:00:00" --until="{target_date_str} 23:59:59" '
        f'--pretty=format:"%h|%an|%ci|%s"',
        cwd=target_dir
    )
    if git_log_raw:
        for line in git_log_raw.splitlines():
            parts = line.split('|', 3)
            if len(parts) == 4:
                info['commits_today'].append({
                    'hash': parts[0].strip(),
                    'author': parts[1].strip(),
                    'date': parts[2].strip(),
                    'message': parts[3].strip()
                })

    # Uncommitted status
    status_raw = run_cmd('git status --porcelain', cwd=target_dir)
    if status_raw:
        for line in status_raw.splitlines():
            if len(line) >= 4:
                status_code = line[:2].strip()
                file_path = line[3:].strip().replace('"', '')
                info['uncommitted_files'].append({
                    'status': status_code,
                    'file': file_path
                })

    # Short diff stat
    diff_stat_raw = run_cmd('git diff --shortstat', cwd=target_dir)
    info['git_diff_stat'] = diff_stat_raw

    return info

def categorize_file(rel_path):
    """Categorize file based on directory and extension."""
    norm = rel_path.replace('\\', '/').lower()
    ext = os.path.splitext(norm)[1]

    if 'database/' in norm or 'migration' in norm or ext == '.sql':
        return 'database'
    if 'api/' in norm or 'service/' in norm or 'controller/' in norm or 'model/' in norm:
        return 'backend-api'
    if 'includes/' in norm or 'helper/' in norm or 'lib/' in norm:
        return 'core-helpers'
    if norm.endswith('.php') or norm.endswith('.html') or norm.endswith('.jsx') or norm.endswith('.tsx') or norm.endswith('.vue'):
        return 'frontend-ui'
    if ext in ('.css', '.scss', '.tailwind', '.js', '.ts'):
        return 'frontend-assets'
    if ext in ('.md', '.txt', '.doc', '.pdf', '.rst') or 'doc' in norm:
        return 'documentation'
    if 'config' in norm or ext in ('.env', '.json', '.yaml', '.yml', '.xml', '.ini'):
        return 'configuration'
    if 'test' in norm:
        return 'testing'
    return 'other'

def scan_filesystem_changes(target_dir, target_date):
    """Scan filesystem for all files with LastWriteTime matching target_date."""
    results = []
    abs_root = os.path.abspath(target_dir)

    for root, dirs, files in os.walk(abs_root):
        # Filter out ignored directories in-place
        dirs[:] = [
            d for d in dirs 
            if d not in DEFAULT_IGNORE_DIRS 
            and not d.startswith('.')
        ]
        
        for f in files:
            if f in DEFAULT_IGNORE_FILES or f.startswith('.'):
                continue
                
            fp = os.path.join(root, f)
            try:
                stat = os.stat(fp)
                mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
                if mtime.date() == target_date:
                    rel_p = os.path.relpath(fp, abs_root)
                    results.append({
                        'file': rel_p.replace('\\', '/'),
                        'time': mtime.strftime('%H:%M:%S'),
                        'timestamp': stat.st_mtime,
                        'size': stat.st_size,
                        'category': categorize_file(rel_p)
                    })
            except (OSError, PermissionError):
                continue

    # Sort chronologically
    results.sort(key=lambda x: x['timestamp'])
    return results

def main():
    parser = argparse.ArgumentParser(description="Detect daily changes across FS timestamps and Git.")
    parser.add_argument('--repo', default='.', help="Repository/project directory path (default: current directory)")
    parser.add_argument('--date', default=None, help="Target date YYYY-MM-DD (default: today)")
    parser.add_argument('--json', action='store_true', help="Output structured JSON")
    parser.add_argument('--markdown', action='store_true', help="Output Markdown formatted report")
    parser.add_argument('--init-log', action='store_true', help="Scaffold docs/devlogs/YYYY-MM/YYYY-MM-DD.md")
    
    args = parser.parse_args()
    
    target_date = datetime.date.today()
    if args.date:
        try:
            target_date = datetime.datetime.strptime(args.date, '%Y-%m-%d').date()
        except ValueError:
            print(f"Error: Invalid date format '{args.date}'. Expected YYYY-MM-DD.", file=sys.stderr)
            sys.exit(1)

    target_date_str = target_date.strftime('%Y-%m-%d')
    fs_changes = scan_filesystem_changes(args.repo, target_date)
    git_info = get_git_info(args.repo, target_date_str)

    data = {
        'date': target_date_str,
        'target_dir': os.path.abspath(args.repo),
        'fs_modified_count': len(fs_changes),
        'fs_modified_files': fs_changes,
        'git': git_info
    }

    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    # Print summary / markdown
    print("=" * 60)
    print(f" 📅 DAILY CHANGE DETECTION REPORT — {target_date_str}")
    print("=" * 60)
    print(f"• Target Directory : {data['target_dir']}")
    print(f"• Git Repository   : {'Yes (Branch: ' + git_info['current_branch'] + ')' if git_info['is_git_repo'] else 'No (Plain Folder)'}")
    print(f"• Git Commits Today: {len(git_info['commits_today'])}")
    print(f"• Files Touched    : {len(fs_changes)} files modified today (FS Timestamp)")
    print("-" * 60)

    if git_info['commits_today']:
        print("\n🔹 Git Commits Recorded Today:")
        for c in git_info['commits_today']:
            print(f"  - [{c['hash']}] {c['message']} ({c['author']})")

    if git_info['uncommitted_files']:
        print(f"\n🔹 Uncommitted Working Tree Files ({len(git_info['uncommitted_files'])}):")
        for u in git_info['uncommitted_files'][:10]:
            print(f"  - [{u['status']}] {u['file']}")
        if len(git_info['uncommitted_files']) > 10:
            print(f"    ... and {len(git_info['uncommitted_files']) - 10} more files")

    print(f"\n🔹 Files Modified on {target_date_str} (by Category):")
    categories = {}
    for item in fs_changes:
        cat = item['category']
        categories.setdefault(cat, []).append(item)

    for cat, items in sorted(categories.items()):
        print(f"\n  📁 [{cat.upper()}] ({len(items)} files):")
        for it in items:
            size_kb = it['size'] / 1024.0
            print(f"    • [{it['time']}] {it['file']} ({size_kb:.1f} KB)")

    if args.init_log:
        month_dir = os.path.join(args.repo, 'docs', 'devlogs', target_date.strftime('%Y-%m'))
        os.makedirs(month_dir, exist_ok=True)
        log_file = os.path.join(month_dir, f"{target_date_str}.md")
        
        if not os.path.exists(log_file):
            template_content = f"""# 📝 Daily Devlog — {target_date_str}

> **Project:** VUMEDHR Training Management System  
> **Date:** {target_date_str}  
> **Git Branch:** `{git_info['current_branch']}`  
> **Commits Today:** {len(git_info['commits_today'])}  
> **Files Touched:** {len(fs_changes)} files  

---

## 1. 🎯 สรุปภาพรวมประจำวัน (Executive Summary)
- [ระบุเป้าหมายหลักและผลลัพธ์สำคัญของวันนี้]

---

## 2. 🚀 รายการการเปลี่ยนแปลง (Categorized Changes)

### ✨ Added (ฟีเจอร์และส่วนประกอบใหม่)
- [รายการสิ่งที่เพิ่มใหม่]

### 🔄 Changed / Refactored (ปรับปรุงและแก้ไขตรรกะเดิม)
- [รายการสิ่งที่ปรับปรุง]

### 🐛 Fixed (แก้ปัญหาและบั๊ก)
- [รายการปัญหาที่ได้รับการแก้ไข]

### 🗄️ Database / Schema Migrations
- [คำสั่ง SQL หรือตารางที่มีการปรับเปลี่ยน]

---

## 3. 📂 รายการไฟล์ที่เกี่ยวข้อง (Impacted Files Matrix)

| เวลาแก้ไข | หมวดหมู่ | ไฟล์ที่แตะ | ขนาด |
| :---: | :---: | :--- | :---: |
"""
            for it in fs_changes:
                size_kb = it['size'] / 1024.0
                template_content += f"| `{it['time']}` | `{it['category']}` | `{it['file']}` | {size_kb:.1f} KB |\n"

            template_content += f"""
---

## 4. ⚠️ ปัญหาที่พบ & ข้อจำกัด (Known Issues & Blockers)
- [ประเด็นที่ยังค้างคา หรือต้องการทดสอบเพิ่มเติม]

---

## 5. 🔮 สิ่งที่ต้องทำต่อในวันถัดไป (Tomorrow's Priorities)
1. [เป้าหมายลำดับถัดไป]
"""
            with open(log_file, 'w', encoding='utf-8') as f:
                f.write(template_content)
            print(f"\n✅ Initialized devlog scaffold: {log_file}")
        else:
            print(f"\nℹ️ Devlog file already exists: {log_file} (Not overwritten)")

if __name__ == '__main__':
    main()
