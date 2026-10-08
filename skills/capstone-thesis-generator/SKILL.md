---
name: capstone-thesis-generator
description: Autonomous generator of complete 5-chapter Thai University Graduation Project / Capstone Theses (เล่มโครงงานปริญญานิพนธ์ 5 บทฉบับเต็ม) in Microsoft Word (.docx) format. Strictly adheres to formal Thai academic thesis standards (TH Sarabun New, pure black text, zero emojis, 1.5-inch left binding margin, standard academic tables). Features automated SQL schema extraction into individual Data Dictionary tables for all database entities, automated headless Selenium browser screenshot capture with authentication into live web applications, full UI walkthrough (10+ figures with step-by-step element explanations), 12-scenario Black-box test matrices, Likert 5-scale user satisfaction statistical evaluation (x̄, S.D.), and complete appendices (Deployment, SQL DDL, SOP). Trigger on /thesis, /capstone-thesis, /academic-report, /generate-thesis, "ทำเล่มจบ", "สร้างเล่มปริญญานิพนธ์", "ทำรายงานโครงงาน 5 บท", "สร้างเล่มรายงาน 5 บท", "ออกรายงานเล่มจบ docx", or whenever the user wants a full-length, formal 5-chapter graduation project thesis or capstone report.
---

# Capstone Thesis Generator (เล่มโครงงานปริญญานิพนธ์ 5 บทฉบับเต็ม)

Generates **complete, formal 5-chapter Graduation Project Theses / Capstone Reports** in Microsoft Word (`.docx`) format, strictly matching Thai university academic standards (อ้างอิงจากเล่มตัวอย่าง `Example-Km/การออกแบบและพัฒนาเว็บไซต์จัดการเครื่องมือช่าง.docx`).

---

## 🏛️ Core Academic Directives

1. **Zero Emojis & Pure Academic Tone**:
   - ไม่มีอิโมจิหรือสัญลักษณ์กราฟิกหลุดเข้ามาในเอกสาร 100%
   - เนื้อหาทั้งหมดใช้ภาษาทางการเชิงวิชาการ (Formal Academic Thai)
2. **Typography & Styling**:
   - ฟอนต์: `TH Sarabun New` (หัวข้อบท 18pt หนา, หัวข้อย่อย 16pt หนา, เนื้อหา 16pt ปกติ)
   - สีตัวอักษร: สีดำล้วน (`RGB: 0, 0, 0`)
   - ระยะขอบ: ซ้าย 1.5 นิ้ว (สำหรับเย็บเล่ม), บน/ขวา/ล่าง 1.0 นิ้ว, ย่อหน้าเยื้อง 0.5 นิ้ว
3. **Complete Data Dictionary**:
   - **ต้องมีตารางพจนานุกรมข้อมูลแยกรายตารางเดี่ยวสำหรับทุกตารางในฐานข้อมูล** (เช่น 12 ตาราง ต้องมีตารางที่ 3.2 ถึง 3.13 ครบถ้วน) ระบุลำดับ, ชื่อฟิลด์, ชนิดข้อมูล, คีย์/ข้อจำกัด, และคำอธิบาย
4. **Authentic System Walkthrough (Live Screenshots)**:
   - ใช้ Selenium ทำการล็อกอินเข้าสู่ระบบจริงบน Local/Remote Server เพื่อบันทึกภาพหน้าจอจริงครบทุกหน้า
   - ทุกภาพต้องมีหมายเลขกำกับ (รูปที่ 4.X) และข้อความอธิบายองค์ประกอบหน้าจอ ปุ่มกด ฟิลด์กรอกข้อมูล และโฟลว์การทำงานอย่างละเอียด
5. **Quality Assurance & Statistical Evaluation**:
   - ตารางการทดสอบ Black-box Testing Matrix อย่างน้อย 10-12 กรณีทดสอบ (TC-01 ถึง TC-12)
   - ตารางผลการประเมินความพึงพอใจ Likert Scale 5 ระดับ พร้อมคำนวณค่าเฉลี่ย ($\bar{x}$) และส่วนเบี่ยงเบนมาตรฐาน (S.D.)

---

## 🔄 Execution Pipeline

```
[1. Target System Context Discovery]
   ├── Inspect project root, tech stack, codebase
   └── Identify database dump (.sql) and running web server URL
                 ↓
[2. Automated SQL Schema Extraction]
   └── Run scripts/extract_schema.py to parse all CREATE TABLE definitions
                 ↓
[3. Automated Live Browser Screenshot Capture]
   └── Run scripts/capture_screenshots.py via headless Selenium to capture all UI screens
                 ↓
[4. 5-Chapter Content Assembly]
   └── Construct JSON payload adhering to references/CHAPTER_STRUCTURE_GUIDE.md
                 ↓
[5. Formal .docx Compilation]
   └── Compile via scripts/generate_academic_thesis.py (Zero emojis, black text, academic borders)
                 ↓
[6. Verification & Presentation]
   └── Verify paragraphs count (>200), tables count (>15), zero emojis, and present file links
```

---

## 🛠️ Bundled Helper Scripts

### 1. `scripts/generate_academic_thesis.py`
The core `python-docx` compiler that enforces strict university styling, margins, table borders, and image embedding.

### 2. `scripts/extract_schema.py`
Parses `.sql` files or database structures and outputs structured Data Dictionary tables ready for Chapter 3.

```bash
python scripts/extract_schema.py path/to/database.sql schema_extracted.json
```

### 3. `scripts/capture_screenshots.py`
Automates browser login via headless Selenium and captures desktop and mobile responsive views.

```python
from scripts.capture_screenshots import capture_application_screens
captured = capture_application_screens(
    base_url="http://localhost/app",
    login_url="http://localhost/app/login.php",
    username="admin",
    password="password123",
    routes={"dashboard": "index.php", "reports": "reports.php"}
)
```

---

## 📚 5 Canonical Chapters Checklist

- [x] **บทที่ 1 บทนำ**: ที่มาและความสำคัญ, วัตถุประสงค์ 1.2.1-1.2.3, ประโยชน์ที่คาดว่าจะได้รับ, ขอบเขต (กลุ่มตัวอย่าง, ฟังก์ชัน), แผนการดำเนินงาน Gantt Chart 5 เดือน (ตารางที่ 1.1)
- [x] **บทที่ 2 เอกสารและงานวิจัยที่เกี่ยวข้อง**: ทฤษฎีปัญหาการจัดตาราง/ระบบงาน, ตารางเปรียบเทียบ 5 ระบบ (ตารางที่ 2.1), ทฤษฎีเฉพาะทาง (เกณฑ์ภาระงาน/สูตรคำนวณ), เทคโนโลยีที่ใช้
- [x] **บทที่ 3 วิธีการดำเนินงานและการออกแบบระบบ**: ความต้องการเชิงหน้าที่/ความปลอดภัย, ตารางวิเคราะห์กระบวนการ (ตารางที่ 3.1), แผนภาพบริบท (Context Diagram), DFD Level 1, Activity Diagram, **พจนานุกรมข้อมูลครบทุกตารางฐานข้อมูล (ตารางที่ 3.2 ถึง 3.X)**, ER Diagram
- [x] **บทที่ 4 ผลการดำเนินงานและการทดสอบระบบ**: **ภาพหน้าจอจริงของระบบครบทุกหน้า (รูปที่ 4.1 ถึง 4.10+)** พร้อมคำบรรยายใต้ภาพและคำอธิบายองค์ประกอบ, ตารางผลการทดสอบ Black-box (ตารางที่ 4.1), ตารางผลประเมิน Likert Scale รายกลุ่ม ($\bar{x}$, S.D.), ตารางเปรียบเทียบ Before vs After
- [x] **บทที่ 5 สรุปผล อภิปรายผล และข้อเสนอแนะ**: สรุปผลตามวัตถุประสงค์, อภิปรายผลเชิงวิศวกรรม, ปัญหา อุปสรรค และแนวทางแก้ไข, ข้อเสนอแนะในอนาคต
- [x] **ภาคผนวก**: ภาคผนวก ก คู่มือติดตั้งและตั้งค่าระบบ (SOP), ภาคผนวก ข โครงสร้างคำสั่ง SQL (DDL), ภาคผนวก ค คู่มือการปฏิบัติงานสำหรับผู้ใช้
