---
name: trpg-world-builder
description: Zero-to-Play Autonomous TRPG & D&D 5e World Builder & Ingester. Takes ANY theme (One Piece, Doraemon, Minecraft, Cyberpunk, JJK, Super God Gene, Dark Fantasy, Sci-Fi) or raw files in /raw/, scaffolds complete directory structure, runs deep ingestion, performs interactive grill-with-docs alignment, synthesizes 100% dedicated setting classes (no generic 5e fantasy bloat), adapts power systems into 5e homebrew, deploys dice/narrator/session tools, establishes anti-sycophancy GM rules (GEMINI.md) with dynamic character variable expansion & in-session live world ingestion, generates full Obsidian knowledge base, deploys twin subagent skills (Character Creator & Session Exporter), and renders interactive HTML infographics in a single turnkey pipeline. Trigger on /build-world, /setup-campaign, /trpg-world-builder, /create-universe, "เซ็ตอัพโลกใหม่", "สร้างระบบสำหรับ", "สร้างแคมเปญ", "สร้างโลก", or "ingest ข้อมูลและสร้างโลก".
---

# 🌌 Zero-to-Play Autonomous TRPG & D&D 5e World Builder & Ingester

This skill turns any blank folder or raw collection of lore/PDFs into a fully playable, deeply customized, and beautifully indexed D&D 5e / TRPG campaign environment in an autonomous, end-to-end turnkey pipeline.

---

## 🏛️ Autonomous 7-Stage Pipeline

```
[1. Folder Scaffolding] ➔ [2. Deep Ingestion & Lore Extraction] ➔ [3. Interactive Grilling & Rule Alignment]
          ➔ [4. Custom Setting Classes, Dynamic Mutation & GM Directives] ➔ [5. Engine Deployment]
          ➔ [6. Obsidian Knowledge Base Generation] ➔ [7. Twin Subagent Skills & Interactive Infographics]
```

---

### 📁 Stage 1: Directory Scaffolding & Architecture
Automatically initialize the Obsidian vault & project filesystem:
```text
/
├── .agents/skills/               # Specialized subagent skills (character creator, session exporter)
│   ├── {theme}-character-creator/
│   └── session-exporter/
├── /wiki/
│   ├── /concepts/                # Core power systems, custom setting classes, homebrew rules
│   │   ├── /skills/              # Martial arts, spells, techniques, abilities
│   │   └── /world-rules/         # Hard cosmology rules, economic systems
│   ├── /bestiary/                # 5e monster/enemy/boss stat blocks
│   ├── /locations/               # Regions, cities, dungeons, hazards, points of interest
│   ├── /npcs/                    # Key quest givers, antagonists, faction leaders
│   ├── /items/                   # Weapons, artifacts, tech/gadgets, consumables
│   └── /sessions/                # Session recaps and campaign devlogs
├── /party/                       # Player character sheets (/party/{name}.md)
├── /raw/                         # Ingested raw lore, PDFs, rulebooks, and text notes
├── /scripts/                     # Python automation engines (dice, session exporter, voice narrator)
├── /audio/                       # Generated AI voice narrations (.mp3)
├── /docs/adr/                    # Architecture Decision Records
├── GEMINI.md                     # Master Game Master & Wiki Agent Directives
├── PROJECT_SUMMARY.md            # Living project status snapshot
├── CONTEXT.md                    # Domain ubiquitous language & glossary
├── index.md                      # Master Obsidian Table of Contents with [[Wikilinks]]
├── hotcache.md                   # Real-time state & next-session briefing
└── log.md                        # Incremental development and lore ingestion changelog
```

---

### 🔍 Stage 2: Deep Ingestion & Lore Analysis
1. Recursively scan and parse everything inside `/raw/` (PDFs, text files, markdown, web links). If `/raw/` is empty, synthesize canonical world lore from model intelligence.
2. Ingest:
   - **World Cosmology & Tone**: High fantasy, grim realism, sci-fi, horror, or anime/novel setting.
   - **Factions & Power Dynamics**: Ruling empires, rebellious factions, guilds, criminal underworlds.
   - **Cosmic & Environmental Hazards**: Dimensional rules, energy storms, local dangers.
   - **Lore Lexicon**: Capture native terms into `CONTEXT.md`.

---

### 💬 Stage 3: Interactive Grilling & Rule Alignment (Grill-with-Docs)
Interview the user with 3–5 targeted questions to stress-test and align the campaign rules:
1. **Lethality & Survival Mechanics**:
   - E.g. Lingering Injuries at 0 HP? Durability degradation? Hunger/Oxygen meters?
2. **Power System Calibration in D&D 5e**:
   - *Super God Gene*: Geno Points 0-100 Cap per tier, Beast Soul equip slots, Hyper Geno Arts.
   - *One Piece*: Devil Fruit Mastery levels, Haki DCs, Swimming weakness / Seastone vulnerability.
   - *Cyberpunk*: Cyberware Humanity cost, Netrunning nodes, Street Cred vs Corporate Heat.
   - *Jujutsu Kaisen*: Cursed Energy pool (100 pt), Simple Domain reaction, Domain Expansion lethal sure-hit.
3. **Tone & DM Style**: Anti-Sycophancy, transparent open dice calculations, in-game chronometer.

---

### 🛡️ Stage 4: Custom Setting Classes, Dynamic Mutation & GM Directives (`GEMINI.md`)

#### 1. 100% Dedicated Setting Classes (No Generic 5e Fantasy Bloat)
- **Eliminate Generic 5e Classes**: Strip away generic fantasy classes (Fighter, Wizard, Cleric, Rogue, etc.) that break immersion.
- **Synthesize 3–5 Dedicated World Classes** written to `/wiki/concepts/classes_{theme}.md`:
  - *Super God Gene*: Hyper Geno Adept, Sky & Shadow Scout, Beast Soul Commander, Gene Harvester.
  - *One Piece*: Pirate Brawler, Master Swordsman, Sniper Scout, Ship Doctor, Weather Navigator.
  - *Cyberpunk*: Solo Mercenary, Netrunner, Techie Engineer, Street Fixer, Nomad Scout.
  - *Jujutsu Kaisen*: Barrier Master, Cursed Tool Specialist, Shikigami Summoner, Body Reinforcer.
- **Define Custom Mechanics**:
  - Hit Die (d6, d8, d10, d12) and Primary Ability Scores.
  - Native Resource Pools (Stamina, Haki, Cursed Energy, Battery, Toxicity).
  - 2–3 Unique Features per class tied directly to setting lore.

#### 2. Dynamic Character Sheet Mutation (Open-Variable State Tracking)
- **Real-time Character Synchronization**: Whenever new information about a player character emerges (new scars, debt, title, behavioral quirk, relationship, secret technique, mutation, spiritual mark, stamina cap, or dietary record), **immediately update `/party/{name}.md`**.
- **Open-Variable Expansion**: DM is never constrained by rigid template fields. If a new type of stat or tracking information arises, **dynamically create new YAML frontmatter keys or Markdown tracking sections/variables on the fly** to store it permanently.

#### 3. In-Session Living World Ingestion (Runtime Codex Expansion)
- **Zero Knowledge Leakage**: Whenever any new creature, monster, weapon, artifact, martial technique, spell, faction, shelter, or cosmic rule is introduced, discovered, or invented during gameplay:
  - **Immediately create or compound its dedicated Wiki note** in `/wiki/entities/creatures/`, `/wiki/entities/items/`, `/wiki/concepts/skills/`, `/wiki/entities/locations/`, or `/wiki/entities/factions/`.
  - Connect all new pages using `[[Wikilinks]]` and log additions into `wiki/log.md`.
  - The world knowledge base continuously compounds during play, not just during prep time!

#### 4. Game Master Directives (`GEMINI.md`)
- **Anti-Sycophancy Rule**: Never flatter or grant plot armor. Monsters and NPCs act with tactical cunning per their lore traits.
- **No Godmoding**: DM controls NPCs, world reactions, and environment. Never narrate player actions or internal thoughts. Always pause for player decisions.
- **Transparent 5e Math**: Always state DCs and exact formula: `[DC 15 CON Save: 1d20(8) + 4 = 12 -> FAILED]`.

---

### ⚙️ Stage 5: Deploy Automation Engine Scripts
Deploy ready-to-run Python utilities in `/scripts/`:
- `scripts/dice_roller.py`: Impartial CLI 5e math engine supporting standard checks, contested rolls, criticals, and lingering injury tables.
- `scripts/session_exporter.py`: Automated CLI tool generating session markdown recap with **Inventory & Resource Delta** and compacting `hotcache.md`.
- `scripts/narrator.py`: Neural AI Voice Narrator (Microsoft Edge Neural Voice / SAPI) with auto-play.

---

### 📚 Stage 6: Generate Full Obsidian Wiki Knowledge Base
Generate 30+ comprehensive, interconnected Markdown notes with YAML frontmatter and bidirectional `[[Wikilinks]]`:
- `/wiki/concepts/classes_{theme}.md`: Complete rules, progression, and abilities of the dedicated setting classes.
- `/wiki/concepts/character_creation_guide.md`: Step-by-step player creation guide using only setting classes.
- `/wiki/bestiary/`: 5e monster stat blocks with Actions, Bonus Actions, Legendary Actions, and Drops.
- `/wiki/locations/`: Regional lore, environmental hazards, shops, NPC rosters.
- `/wiki/npcs/`: Motivations, stats, dialogues, quest hooks.
- Master `index.md`, `hotcache.md`, `CONTEXT.md`, and `log.md`.

---

### 🎨 Stage 7: Twin Subagent Skills & Interactive Infographics

#### 1. Subagent Skill 1: Character Creator
- **Path**: `.agents/skills/{theme}-character-creator/SKILL.md`
- **Trigger**: `/create-character`, "สร้างตัวละคร", "ลงทะเบียนตัวละคร"
- **Function**: Conducts an interactive 4-step interview presenting the setting's custom classes, standard array, and generates `/party/{name}.md`.

#### 2. Subagent Skill 2: Session Exporter
- **Path**: `.agents/skills/session-exporter/SKILL.md`
- **Trigger**: `/export-session`, "ส่งออกเซสชัน", "สรุปเซสชัน", "บันทึกการเล่น", "จบเซสชัน"
- **Function**: Autonomously scans chat conversation, extracts narrative events, combat outcomes, resource/EXP/Geno deltas, writes `/wiki/sessions/session_{number}_{date}.md`, updates player sheets in `/party/{name}.md`, and refreshes `hotcache.md` for next-session launch.

#### 3. Interactive Infographics Codex
- **Path**: `{theme}_codex.html`
- **Features**: Standalone HTML5 with responsive tabs (Custom Classes, Power Progression, Bestiary, Gear & Loot, Rules & Injuries) viewable in any browser.

#### 4. Session 1 Launch
- High-density prologue briefing in `hotcache.md` ready for the player to step into the world!