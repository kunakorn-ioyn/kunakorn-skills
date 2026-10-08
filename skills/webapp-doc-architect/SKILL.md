---
name: webapp-doc-architect
description: Extracts web application project information, source code, schemas, and documentation to generate industry-standard user manuals, technical architecture documentation, Word documents (.docx), PowerPoint presentations (.pptx), and printable PDF manuals. Use when creating manuals, user guides, API docs, system specifications, or presentation slide decks from an existing project workspace.
---

# webapp-doc-architect

Automates the discovery, extraction, and generation of enterprise-grade software manuals, user guides, technical specifications, and presentation slide decks directly from web application workspaces and project documentation.

Summary

This skill inspects existing project source code, database definitions, API routes, environment files, and internal notes to synthesize comprehensive, production-ready documentation conforming to international documentation standards (such as Diataxis and IEEE 1063). It can output Word documents (.docx), PowerPoint presentations (.pptx), and PDF-ready manuals.

When to Use

When the user asks to generate a user manual, operator handbook, or standard operating procedure (SOP) for their web application.

When generating technical architecture documentation, API endpoint references, or database schema manuals from an existing repository.

When creating executive slide decks or training presentations (.pptx) summarizing system features and workflows.

When turning project notes and codebase knowledge into formatted Word (.docx) documents or PDF manuals.

When organizing system documentation following structured international frameworks.

Workflow

1. Ingest and Analyze Project Sources

Before writing documentation, inspect the workspace to extract accurate system knowledge:

Technology Stack & Dependencies: Scan package.json, composer.json, pyproject.toml, pom.xml, go.mod, or Dockerfiles to identify frameworks, libraries, runtime environments, and service dependencies.

Application Routing & API Contracts: Inspect routes and controllers (routes/, controllers/, api/, endpoints/, or OpenAPI/Swagger JSON/YAML specs) to extract endpoints, HTTP methods, request payloads, and status codes.

Data Models & Database Schema: Examine ORM definitions and migrations (schema.prisma, models/, migrations/, SQL scripts) to reconstruct data entities, field data types, relationships, and constraints.

Configuration & Environment: Review .env.example, config files, and deployment descriptors to extract environment variables and external integrations.

Existing Documentation: Search for README.md, docs/, design specs, changelogs, and inline docstrings to gather business rules and background context.

Access Control & Roles: Identify user roles, authentication flows (e.g., JWT, OAuth2, session-based), and authorization gates.

2. Classify Document Type and Target Audience

Determine the format and structure matching the user's intent:

End-User / Operations Manual (Diataxis How-to / Tutorial Style):

Audience: End-users, operational staff, managers.

Structure: System overview, access & login procedures, role-based workflows, step-by-step task instructions with UI callouts, FAQs, and error troubleshooting.

Technical Architecture & Developer Guide (Diataxis Reference / Explanation Style):

Audience: Developers, DevOps engineers, system administrators.

Structure: Architectural topology, component interaction, data dictionary (ERD), API catalog with parameters and response models, environment variable dictionary, security policies, and deployment steps.

Executive Overview / Training Deck (PowerPoint Presentation):

Audience: Stakeholders, business clients, new team members.

Structure: High-level value proposition, system architecture visual, feature modules breakdown, core user journey, security & compliance overview, and maintenance roadmap.

3. Generate Deliverables

Generate concrete, production-ready files via Python scripts in the execution environment:

A. Microsoft Word Manual (.docx)

When Word output is requested, use python-docx with the following conventions:

Title Page: Document title, subtitle, target system version, author/organization, and publication date.

Heading Hierarchy: Use consistent styles (Heading 1, Heading 2, Heading 3) with distinctive accent colors (e.g., Deep Navy #1E3A8A for primary headers).

Callout Boxes: Represent warnings, tips, and prerequisites inside single-cell shaded tables with left border accents.

Reference Tables: Format API endpoints and database fields in tables with styled header rows, alternating background colors, and clear column widths.

Action Steps: Use bold text for all UI elements (e.g., "Click Save Changes in the upper right toolbar").

# Example generator snippet for python-docx
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()
# Configure styles, title page, content tables, and callouts


B. PowerPoint Slide Deck (.pptx)

When PowerPoint output is requested, use python-pptx with widescreen (16:9) slides:

Slide Aspect Ratio: Set slide dimensions to 13.333 x 7.5 inches (Inches(13.333), Inches(7.5)).

Consistent Color Palette: Choose an authoritative 3-color palette (e.g., Navy #0F172A, Slate #475569, Cyan/Blue Accent #2563EB).

Structured Cards: Instead of dense text blocks, display features and workflows as distinct geometric card boxes with headers and bullet points.

Slide Blueprint:

Title Slide: System name, tagline, presenter, date.

Executive Summary: Core problem solved and key metrics.

System Architecture & Tech Stack: Component diagram and services.

Core Feature Modules: 2-3 slides grouping capabilities logically.

End-to-End User Journey: Linear process flow.

API & Data Overview: Key data entities and integration capabilities.

Security & Deployment: Authentication model and hosting infrastructure.

Summary & Next Steps: Support channels and contact information.

# Example generator snippet for python-pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
# Add slides, headers, cards, and accent shapes


C. Printable PDF Manual

When PDF output is requested:

Generate a clean, responsive HTML document with CSS print styles (@media print, @page { margin: 20mm; }, page-break rules).

Convert the HTML to PDF using available environment tools (such as weasyprint, wkhtmltopdf, or Chrome headless print), or format markdown for immediate export.

Ensure page numbers and running headers/footers appear on all content pages.

D. System Flow and Architecture Diagrams

Always embed or supply Mermaid.js syntax for visual representation:

Entity Relationship Diagram (ERD): For database schemas and foreign key relations.

Sequence Diagram: For authentication, payment, or complex asynchronous job lifecycles.

Flowchart: For multi-step business logic and approval workflows.

4. Quality Standards and Technical Writing Rules

Use active voice and imperative mood for all instructional steps (e.g., "Select the target project from the dropdown", not "The project should be selected").

Clearly declare required permissions or user roles at the beginning of each procedure.

Document error handling: for every critical workflow, specify what error messages might appear and how the user can resolve them.

Format all API parameters and config keys in monospaced code formatting.

Gotchas

Do not invent hypothetical endpoints, database fields, or features if actual project files exist in the repository; always ground details in the real codebase.

Avoid cluttered PowerPoint slides; keep slide text concise with visual groupings.

Check library availability (python-docx, python-pptx) before running generation scripts, and handle missing dependencies cleanly.

Never output raw unmasked secrets, real API keys, or production database credentials in generated manuals.