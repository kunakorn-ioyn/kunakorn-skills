---
name: visual-entity-forge
description: Autonomously analyzes user-provided images of beasts, monsters, weapons, treasures, or powers, and creatively designs lore-accurate entities for the Super God Gene TRPG world (God's Sanctuary). Formulates complete D&D 5e monster stat blocks, geno point nutrition, beast soul drop types, combat tactics, and habitat lore, immediately writing them into /wiki/entities/ with [[Wikilinks]] and updating the codex log. Trigger on /forge-entity, /create-beast, /image-to-beast, "ออกแบบจากรูป", "เพิ่มสิ่งมีชีวิตจากรูป", "สร้างมอนสเตอร์จากภาพ", "ดูรูปนี้แล้วสร้าง", or whenever the user uploads or mentions an image to turn into a creature, item, or power.
---

# 🎨 Visual Entity Forge (ระบบเนรมิตสิ่งมีชีวิตและไอเทมจากภาพ)

สกิลสำหรับวิเคราะห์ภาพวาด รูปถ่าย หรืออาร์ตเวิร์กที่ผู้ใช้ส่งเข้ามา แล้วสกัดรูปลักษณ์ ออร่า สรีระ นำมารังสรรค์เป็น **สิ่งมีชีวิต (สัตว์อสูร), อาวุธ/ไอเทม, หรือวิชาพลัง** ที่สอดคล้องกับโลก **Super God Gene (ก็อตแซงชัวรี่)** พร้อมสเตตัส D&D 5e เต็มรูปแบบ และนำเข้าคลังวิกิ (`/wiki/`) ทันที!

---

## 🧭 Workflow การทำงาน 5 ขั้นตอน

```mermaid
flowchart TD
    A[รับภาพจากผู้ใช้] --> B[Visual Feature Extraction<br/>วิเคราะห์สรีระ / สี / ออร่า / จุดเด่น]
    B --> C[Lore & Tier Mapping<br/>จัดระดับชั้น สามัญ/กลายพันธุ์/เลือดศักดิ์สิทธิ์/ซูเปอร์]
    C --> D[D&D 5e Stat Block & Drops<br/>คำนวณ HP, AC, ท่าโจมตี, วิญญาณอสูร, แต้มจีโน]
    D --> E[Codex Ingestion & Linking<br/>เขียนลง /wiki/entities/ พร้อม [[Wikilinks]] & Log]
```

---

### ขั้นตอนที่ 1: Visual Feature Extraction (ถอดรหัสจากภาพ)
สังเกตองค์ประกอบในภาพอย่างละเอียด:
1. **สรีระและโครงสร้าง (Anatomy)**:
   - รูปร่างพื้นฐาน (แมลง, สัตว์เลื้อยคลาน, นกยักษ์, สัตว์สี่ขา, มนุษย์อสูร, โครงกระดูก)
   - อวัยวะเด่น: ก้ามหนา, เขาแหลม, ปีกคู่, หางมีพิษ, เกล็ดเกราะ, คมเขี้ยว
2. **ธาตุและออร่า (Element & Atmosphere)**:
   - แสงสีรอบตัว: สีทอง (เลือดศักดิ์สิทธิ์/แสง), สีม่วง/ดำ (ทมิฬ/พิษ/มิติ), สีแดงเพลิง (เพลิงโลกันตร์), สีฟ้าคราม (น้ำแข็ง/สายฟ้า)
   - บรรยากาศ: ดุร้าย, ลึกลับ, สง่างาม, น่าสะพรึงกลัว
3. **ขนาดและระดับภัยคุกคาม (Scale & Threat)**:
   - ขนาดตัวเทียบกับมนุษย์ (Tiny, Small, Medium, Large, Huge, Gargantuan)

---

### ขั้นตอนที่ 2: God's Sanctuary Lore Mapping (การจัดลำดับชั้นในแซงชัวรี่)

กำหนดระดับชั้นให้สอดคล้องกับความน่าเกรงขามในภาพ:

| ระดับ (Tier) | ลักษณะเด่น | โภชนาการ (Geno Points) | วิญญาณอสูร (Drop Chance) |
|---|---|---|---|
| **สามัญ (Ordinary)** | ร่างกายแข็งแกร่งกว่าสัตว์ป่าโลกเดิมเล็กน้อย อาวุธเหล็กพอทำร้ายได้ | กินเนื้อได้ **จีโนพ้อยท์สามัญ** (0–10 แต้ม) | ดรอปอัตรา 1% (1d100 = 100) |
| **กลายพันธุ์ (Mutant/Primitive)** | เกราะหนาดุจหินผา มีพลังธาตุเบื้องต้น อาวุธทั่วไปฟันแทบไม่เข้า | กินเนื้อได้ **จีโนพ้อยท์กลายพันธุ์** (0–10 แต้ม) | ดรอปอัตรา 5% (1d100: 96–100) |
| **เลือดศักดิ์สิทธิ์ (Sacred-Blood)** | ประกายออร่าเปล่งประกาย สติปัญญาเฉียบแหลม อาวุธระดับต่ำหักสะบั้น | กินเนื้อได้ **จีโนพ้อยท์เลือดศักดิ์สิทธิ์** (0–10 แต้ม) | ดรอปอัตรา 10% (1d100: 91–100) |
| **ซูเปอร์มอนสเตอร์ (Super Beast)** | พลังทลายขุนเขา จ่าฝูงแห่งแดนศักดิ์สิทธิ์ มนุษย์ทั่วไปแตะต้องไม่ได้ | สกัดได้ **แก่นชีวิตซูเปอร์ (Life Essence)** | ดรอปอัตรา 25% (1d100: 75–100) |

#### กำหนดชนิดวิญญาณอสูร (Beast Soul Type):
- **เกราะ (Armor)**: จากมอนสเตอร์ที่มีกระดอง เกล็ดหนา หรือผิวหนังแกร่ง
- **อาวุธ (Weapon)**: หอก, ดาบ, ธนู, กริช จากมอนสเตอร์ที่มีกรงเล็บ คมดาบ หรือฟันแหลม
- **ปีกบิน (Wings)**: จากมอนสเตอร์มีปีก
- **สัตว์ขี่ (Mount)**: จากมอนสเตอร์สี่ขา ร่างใหญ่ ว่องไว
- **แปลงร่าง (Morph/Transformation)**: มอนสเตอร์รูปร่างพิเศษที่มอบบัฟพลังกายภาพมหาศาล
- **สัตว์อสูรช่วยรบ (Combat Pet)**: สัตว์อสูรตัวเล็ก คล่องแคล่ว ช่วยสอดแนมหรือต่อสู้

---

### ขั้นตอนที่ 3: D&D 5e Stat Block & Combat Design

สร้าง Stat Block ที่พร้อมนำไปทอยเต๋าเล่นได้จริง:
- **Armor Class (AC)** และ **Hit Points (HP)**
- **Speed**: เดิน, บิน, ไต่กำแพง, ว่ายน้ำ, ขุดดิน
- **Ability Scores**: STR, DEX, CON, INT, WIS, CHA พร้อม Modifier
- **Damage Resistances / Vulnerabilities / Immunities**
- **Senses**: Darkvision, Blindsight, Tremorsense
- **Traits**: 1–2 คุณสมบัติพิเศษตามรูปลักษณ์ (เช่น *เกราะสะท้อนแสง, พิษกัดกร่อนกระดูก, ซุ่มโจมตีในทราย*)
- **Actions**: Multiattack, กรงเล็บ, เขี้ยวพิษ, ท่าพ่นธาตุ (DC Save)
- **Legendary Actions**: (เฉพาะระดับเลือดศักดิ์สิทธิ์ หรือ ซูเปอร์มอนสเตอร์)

---

### ขั้นตอนที่ 4: Codex Ingestion (บันทึกเข้าวิกิแบบเรียลไทม์)

1. **สร้างไฟล์วิกิ**:
   - ถ้าเป็นสัตว์อสูร: `/wiki/entities/creatures/<ชื่อสัตว์อสูร>.md`
   - ถ้าเป็นอาวุธ/สมบัติ: `/wiki/entities/items/<ชื่อไอเทม>.md`
   - ถ้าเป็นวิชา/พลัง: `/wiki/concepts/skills/<ชื่อวิชา>.md`
2. **ใส่ YAML Frontmatter มาตรฐาน**:
   ```yaml
   ---
   type: creature
   title: "ชื่อสัตว์อสูร (ภาษาไทย / อังกฤษ)"
   tier: "Ordinary | Primitive | Sacred-Blood | Super"
   habitat: "[[wiki/entities/locations/ชื่อสถานที่]]"
   beast_soul: "ชนิดวิญญาณอสูร"
   geno_nutrition: "ประเภทจีโนพ้อยท์"
   tags:
     - bestiary
     - creature
     - god-sanctuary
   ---
   ```
3. **เชื่อมโยง `[[Wikilinks]]`**: เชื่อมไปยังสถานที่อยู่อาศัย, ทรัพยากรที่เกี่ยวข้อง
4. **บันทึกลง `wiki/log.md`**: บันทึกการเพิ่มข้อมูลใหม่
5. **รีเฟรช `wiki/hotcache.md`**: ดึงข้อมูลสรุปเข้าหน่วยความจำด่วน

---

### ขั้นตอนที่ 5: นำเสนอแก่ผู้เล่นอย่างน่าตื่นเต้น

ส่งคำอธิบายสไตล์นิยายแฟนตาซี ให้ผู้เล่นเห็นภาพความน่าเกรงขาม พร้อมตาราง Stat Block และรายละเอียดวิญญาณอสูรที่รอให้ผู้เล่นไปพิชิต!
