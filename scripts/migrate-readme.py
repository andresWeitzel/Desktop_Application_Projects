from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ICON_PATHS = {
    "csharp": "assets/icons/backend/others/png/csharp.png",
    "vsc": "assets/icons/devops/png/vsc.png",
    "mysql": "assets/icons/database/png/mysql.png",
    "postgres": "assets/icons/database/png/postgres.png",
    "dbeaver": "assets/icons/database/png/dbeaver.png",
    "docker": "assets/icons/devops/png/docker.png",
    "postman": "assets/icons/devops/png/postman.png",
    "git": "assets/icons/devops/png/git.png",
    "java": "assets/icons/backend/java/png/java.png",
    "maven": "assets/icons/devops/png/maven.png",
    "netbeans": "assets/icons/backend/java/png/netbeans.png",
}

CLUB_ICONS = ["git", "postman", "dbeaver", "vsc", "mysql", "csharp"]
JAVA_ICONS = ["git", "postman", "maven", "mysql", "netbeans", "java"]
FITNESS_MANAGER_ICONS = ["git", "postman", "maven", "docker", "postgres", "java"]

PROJECTS = [
    {
        "id": "fitness-manager-platform",
        "title_es": "Plataforma de Gestión Fitness",
        "title_en": "Fitness Manager Platform",
        "repo": "https://github.com/andresWeitzel/Fitness_Training_Management_Platform-Desktop",
        "image": "Fitness Manager Platform.png",
        "icons": FITNESS_MANAGER_ICONS,
    },
    {
        "id": "sports-club-management",
        "title_es": "Gestión de Club Deportivo",
        "title_en": "Sports Club Management",
        "repo": "https://github.com/andresWeitzel/DSOO_ClubDeportivo",
        "image": "Sports Club Management.png",
        "icons": CLUB_ICONS,
    },
    {
        "id": "employee-management-and-reporting",
        "title_es": "Gestión y Reportes de Empleados",
        "title_en": "Employee Management and Reporting",
        "repo": "https://github.com/andresWeitzel/Gestor_de_Empleados",
        "image": "Employee Management and Reporting.png",
        "icons": JAVA_ICONS,
    },
    {
        "id": "drug-control-for-chimpanzees",
        "title_es": "Control de Fármacos en Chimpancés",
        "title_en": "Drug Control for Chimpanzees",
        "repo": "https://github.com/andresWeitzel/Farmaco_NTZ184",
        "image": "Drug Control for Chimpanzees.png",
        "icons": JAVA_ICONS,
    },
    {
        "id": "personal-expense-management",
        "title_es": "Gestión de Gastos Personales",
        "title_en": "Personal Expense Management",
        "repo": "https://github.com/andresWeitzel/Gestor_Gastos_Personales",
        "image": "Personal Expense Management.png",
        "icons": JAVA_ICONS,
    },
]

SPANISH_FLAGS = """<div align="right">
    <a href="./README.md" target="_blank" title="Español">
      <img src="./doc/assets/img/arg-flag.jpg" width="65" height="40" alt="Español" />
    </a>
    <a href="./translations/README.en.md" target="_blank" title="English">
      <img src="./doc/assets/img/eeuu-flag.jpg" width="65" height="40" alt="English" />
    </a>
</div>"""

ENGLISH_FLAGS = """<div align="right">
    <a href="../README.md" target="_blank" title="Español">
      <img src="../doc/assets/img/arg-flag.jpg" width="65" height="40" alt="Español" />
    </a>
    <a href="./README.en.md" target="_blank" title="English">
      <img src="../doc/assets/img/eeuu-flag.jpg" width="65" height="40" alt="English" />
    </a>
</div>"""


def icon_tag(name: str, prefix: str) -> str:
    return (
        f'<img width="25" height="25" src="{prefix}/{ICON_PATHS[name]}" '
        f'style="vertical-align: middle;" border="0" />'
    )


def icon_row(names: list[str], prefix: str, align: str = "left") -> str:
    tags = " ".join(icon_tag(name, prefix) for name in names)
    return f'  <div align="{align}">{tags}</div>'


def details_block(repo: str, prefix: str, *, spanish: bool) -> str:
    pill = "codigo-pill.png" if spanish else "code-pill.png"
    title = "Código" if spanish else "Code"
    alt = title
    return f"""<div align="center">
<a href="{repo}" target="_blank" rel="noopener noreferrer" title="{title}"><img src="{prefix}/assets/icons/detail-actions/{pill}" alt="{alt}" height="30" border="0" /></a>
</div>"""


def project_section(project: dict, prefix: str, *, spanish: bool) -> str:
    title = project["title_es"] if spanish else project["title_en"]
    details_label = "Detalles" if spanish else "Details"
    icons = icon_row(project["icons"], prefix, align="right")
    return f""" <!------START {project['id']}------>

<div align="center">
  
<a id="{project['id']}"></a>
### {title} ![status-completed]({prefix}/assets/icons/badges/status-completed.svg)

<a href="{project['repo']}" target="_blank">
  <img src="{prefix}/assets/img/projects/{project['image']}" >
</a>

{icons}

<br>

 ### {details_label}

{details_block(project['repo'], prefix, spanish=spanish)}
   
<!------END {project['id']}------->

</div>

<br>
<br>
<br> 
<br>
"""


def index_section(prefix: str, *, spanish: bool) -> str:
    lines = []
    for project in PROJECTS:
        title = project["title_es"] if spanish else project["title_en"]
        lines.append(
            f"* [{title} ![status-completed]({prefix}/assets/icons/badges/status-completed.svg)](#{project['id']})"
        )
        lines.append("")
        lines.append(icon_row(project["icons"], prefix, align="left"))
        lines.append("")
    return "\n".join(lines)


def build_readme(*, spanish: bool) -> str:
    prefix = "./doc" if spanish else "../doc"
    flags = SPANISH_FLAGS if spanish else ENGLISH_FLAGS
    title = "Aplicaciones de Escritorio" if spanish else "Desktop App"
    intro = (
        "Repositorio central para aplicaciones de escritorio que digitalizan la operación interna de organizaciones: administración de registros y usuarios, cobros y control operativo, reportes analíticos, interfaces gráficas con Swing y Windows Forms, persistencia relacional y no relacional, y despliegue local y productivo."
        if spanish
        else "Central repository for desktop applications that digitize internal organizational operations: records and user administration, billing and operational control, analytical reporting, Swing and Windows Forms GUIs, relational and non-relational persistence, and local and production deployment."
    )
    tech_lines = (
        [
            "  * Lenguajes: Java, C#, otros.",
            "  * Frameworks: Swing, Windows Forms, JavaFX, JDBC, otros.",
            "  * Tecnologías: Java SE, .NET, Maven, otros.",
            "  * Bases de datos: MySQL, MariaDB, PostgreSQL, otros.",
            "  * Librerías: mysql-connector, JFreeChart, JCommon, ADO.NET, otros.",
            "  * Herramientas: NetBeans, VSC, Git, Postman, XAMPP, DBeaver, Docker, otros.",
            "  * Patrones: DAO, Singleton, otros.",
        ]
        if spanish
        else [
            "  * Languages: Java, C#, others.",
            "  * Frameworks: Swing, Windows Forms, JavaFX, JDBC, others.",
            "  * Technologies: Java SE, .NET, Maven, others.",
            "  * Databases: MySQL, MariaDB, PostgreSQL, others.",
            "  * Libraries: mysql-connector, JFreeChart, JCommon, ADO.NET, others.",
            "  * Tools: NetBeans, VSC, Git, Postman, XAMPP, DBeaver, Docker, others.",
            "  * Patterns: DAO, Singleton, others.",
        ]
    )
    index_title = "Índice 📜" if spanish else "Index 📜"
    index_summary = " Ver " if spanish else " See "
    projects_heading = "🗂️ Proyectos" if spanish else "🗂️ Projects"
    projects_section_title = "🗂️ Proyectos" if spanish else "🗂️ Projects"
    index_projects_heading = "🗂️ Proyectos" if spanish else "🗂️ Projects"

    projects_body = "\n".join(project_section(project, prefix, spanish=spanish) for project in PROJECTS)

    return f"""<div align = "center">
<img src="{prefix}/assets/img/projects/desktop-app.png" >
</div>

<br>

{flags}

<div align="center">
  
##  <img width="36" height="48" src="{prefix}/assets/gifs/desktop.gif" />  {title}

</div>

</br>


{intro}
 
<br>

{chr(10).join(tech_lines)}
   
<br>
<br>

<!------Start Index----->

<a id="index"></a>
## {index_title}

<details>
 <summary>{index_summary}</summary>

 <br>

#### {index_projects_heading}

{index_section(prefix, spanish=spanish)}
<br>

</details>

<!------Stop Index----->
  
<br>
<br>

<div align="center">
    
 ## {projects_section_title}

</div>

<br>

{projects_body}"""


def main() -> None:
    es_path = ROOT / "README.md"
    en_path = ROOT / "translations" / "README.en.md"
    old_es = ROOT / "translations" / "README.es.md"

    en_path.parent.mkdir(parents=True, exist_ok=True)
    es_path.write_text(build_readme(spanish=True), encoding="utf-8", newline="\n")
    en_path.write_text(build_readme(spanish=False), encoding="utf-8", newline="\n")

    if old_es.exists():
        old_es.unlink()

    print(f"updated {es_path}")
    print(f"updated {en_path}")
    if not old_es.exists():
        print("removed translations/README.es.md")


if __name__ == "__main__":
    main()
