---
name: km-system-report-generator
description: Autonomous generator of official, comprehensive Knowledge Management (KM) and Full System Engineering Reports in Microsoft Word (.docx) format. Integrates deep codebase analysis, system case studies, official university/enterprise KM standards, mathematical formulas, and database dictionaries into formal documents with executive summaries, styled tables, callout boxes, and custom typography. Trigger on /km-report, /full-report, /generate-doc, "สร้างรายงานฉบับเต็ม", "ทำเอกสาร KM", "สร้างรายงาน Word", "ออกรายงานระบบ docx", or whenever the user wants a full-length, formal project or KM report.
---

# KM & Full System Report Generator

Transform codebase architecture, system specifications, and engineering case studies into **official, comprehensive Microsoft Word (`.docx`) Knowledge Management (KM) and System Engineering Reports** aligned with university standards and the reference template in `Ex-Km/` (`ขั้นตอนที่ 2 การสร้างและแสวงหาความรู้ KM 2569_VUMED.docx`).

---

## 🎯 Official Reference Standard (`Ex-Km/`)

The generated KM document adheres strictly to the official university KM framework:
1. **Title & Header Standard**:
   - แผนการดำเนินงานจัดการความรู้ (Knowledge Management: KM)
   - คณะแพทยศาสตร์ มหาวิทยาลัยวงษ์ชวลิตกุล (หรือหน่วยงานที่ระบุ) ประจำปีการศึกษา 2569
   - โครงการ: [ชื่อระบบ เช่น ระบบจัดการตารางสอนและภาระงาน LearnPlan]
   - ขั้นตอนที่ 2 การสร้างและแสวงหาความรู้ (Knowledge Creation & Acquisition)
2. **Structure & Canonical Sections**:
   - **เป้าหมายสำคัญ (Core Objective)**: การแสวงหาความรู้ภายใน/ภายนอก (Explicit & Tacit) และการสร้างองค์ความรู้ใหม่
   - **1. กระบวนการสร้างและแสวงหาความรู้ (KM Process)**:
     - 1.1 การค้นหาและแสวงหาความรู้ที่มีอยู่ (External & Internal Discovery)
     - 1.2 การวิเคราะห์ปัญหา อุปสรรค และโอกาสในการต่อยอด
     - 1.3 การสร้างองค์ความรู้ใหม่ (Knowledge Creation - โครงสร้างข้อมูลดิจิทัล, Digital Workflow, Dashboard)
     - 1.4 การเรียบเรียงและรวบรวมเป็นฐานความรู้ (Knowledge Codification)
   - **2. สรุปผลการศึกษาและรวบรวมความรู้จากเอกสารเกณฑ์เดิม (Explicit Knowledge Tables)**:
     - ตารางแจกแจงเกณฑ์มาตรฐานและข้อบังคับ
   - **3. สรุปโครงสร้างสูตรคำนวณแบบ Real-time**:
     - รูปแบบที่ 1: เชิงเทคนิค (Technical Specification & Algorithm Model สำหรับวิศวกร/นักพัฒนา)
     - รูปแบบที่ 2: สำหรับทำเอกสาร KM (KM Document Standard Representation สำหรับผู้บริหาร/ผู้ประเมิน)
     - คุณสมบัติการประมวลผล Real-time (Dynamic Scaling, Multi-Role Distribution, Threshold Checking)

---

## 🔄 Turnkey Workflow

```
[1. Target System & Mode Selection]
                 ↓
[2. Deep Ingestion (Codebase, Case Study, Database Schema, ADRs)]
                 ↓
[3. Chapter Structure Synthesis (JSON Schema)]
                 ↓
[4. Automated .docx Generation via python-docx Engine]
                 ↓
[5. Final Document Presentation & Verification]
```

---

## Standard Chapter Structure for Full KM Report

When generating a KM / Full System Report, ensure the following 6-tier canonical chapters are populated:

### 📑 Metadata & Executive Summary
- **Title**: โครงการพัฒนาระบบ... (ระบบจัดการความรู้และภาระงาน...)
- **Subtitle**: แผนการดำเนินงานจัดการความรู้ (Knowledge Management: KM) คณะ... ประจำปีการศึกษา...
- **Executive Summary Box**: สรุปเป้าหมาย คอขวดเดิม แนวทางแก้ไข และตัวชี้วัดความสำเร็จหลัก (1 หน้าแรก)

### 📖 บทที่ 1: ความเป็นมา วัตถุประสงค์ และกรอบยุทธศาสตร์
- ปัญหาและความจำเป็น (Pain Points & Bottlenecks)
- วัตถุประสงค์และเป้าหมายเชิงยุทธศาสตร์
- ขอบเขตของระบบและกลุ่มผู้ใช้งานเป้าหมาย

### 🧠 บทที่ 2: การสร้าง แสวงหา และรวบรวมองค์ความรู้ (Explicit & Tacit Knowledge)
- การสกัดกฎเกณฑ์ ข้อบังคับ และระเบียบขององค์กร (Explicit Knowledge)
- องค์ความรู้เชิงประสบการณ์และแนวทางปฏิบัติงานจริง (Tacit Knowledge)
- สูตรและเกณฑ์การคำนวณแบบมาตรฐาน (Mathematical & Logical Models)

### 🏗️ บทที่ 3: สถาปัตยกรรมระบบ การออกแบบเชิงเทคนิค และความมั่นคงปลอดภัย
- โครงสร้างสถาปัตยกรรม (High-Level Architecture & Single-Entry REST API)
- พจนานุกรมข้อมูลและฐานข้อมูล (Database Dictionary & Relationships)
- กลไกการตรวจจับความขัดแย้งและคำนวณแบบ Real-time
- มาตรการความปลอดภัย (OAuth 2.0, RBAC, .htaccess Protection)

### 👥 บทที่ 4: กระบวนการใช้งาน การจัดเก็บ และการกระจายความรู้
- แผนผังกระบวนการทำงาน (Workflow & User Journey)
- บทบาทและสิทธิ์การเข้าถึง (Admin, Coordinator, Faculty, Staff, Student)
- ระบบแจ้งเตือนและระบบส่งออกข้อมูล (LINE Bot, PDF A4 Landscape, Excel)

### 📊 บทที่ 5: ผลการประเมิน ตัวชี้วัด และประโยชน์ที่ได้รับ
- ตารางเปรียบเทียบก่อน-หลังนำระบบไปใช้ (Before vs After Performance Matrix)
- ตัวชี้วัดด้านเวลา ความแม่นยำ และความพึงพอใจ
- ความคุ้มค่าและผลกระทบเชิงองค์กร

### 🚀 บทที่ 6: บทเรียนหน้างาน และแนวทางการพัฒนาต่อยอด
- ปัญหาอุปสรรคและแนวทางแก้ไข (Lessons Learned & Troubleshooting)
- แผนการขยายผลและพัฒนาในระยะถัดไป (Future Roadmap)

---

## 🛠️ Execution Engine

To compile and produce the final Word document, structure the report as a JSON payload and run the bundled Python script:

```bash
python .agents/skills/km-system-report-generator/scripts/generate_docx_report.py \
  --input-json path/to/report_structure.json \
  --output path/to/output_document.docx
```
