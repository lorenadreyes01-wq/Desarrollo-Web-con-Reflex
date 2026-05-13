# 🌸 Beauty Cosmetics Clone — Reflex + Poetry

> Proyecto educativo desarrollado con **Reflex** que replica una landing page moderna de cosméticos y beauty ecommerce inspirada en interfaces minimalistas y elegantes.

---

# 📸 Vista previa

Diseño inspirado en:

* Beauty Ecommerce UI
* Shopify Cosmetics Stores
* Modern Landing Pages
* Soft Pink Aesthetic

La aplicación incluye:

* Hero Section
* Productos destacados
* Banner promocional
* Categorías beauty
* Footer responsive

---

# Tecnologías utilizadas

* [Reflex](https://reflex.dev/?utm_source=chatgpt.com)
* [Poetry](https://python-poetry.org/?utm_source=chatgpt.com)
* Python 3.10+
* Node.js 18+

---

# 📂 Estructura oficial del proyecto

```text
DESARROLLO-WEB-CON-REFLEX/
│
├── .states/
├── .venv/
├── .web/
├── .vscode/
│
├── assets/
│
├── Desarrollo_Web_con_Reflex/
│   ├── __init__.py
│   └── Desarrollo_Web_con_Reflex.py
│
├── .gitignore
├── poetry.lock
├── pyproject.toml
├── README.md
└── rxconfig.py
```

---

# 📦 Requisitos previos

Instalar:

* Python 3.10+
* Node.js 18+
* Poetry
* Git

---

# 📥 Clonar el repositorio

```bash id="6l6grq"
git clone https://github.com/lorenadreyes01-wq/Desarrollo-Web-con-Reflex.git
```

Entrar al proyecto:

```bash id="2jlwmx"
cd Desarrollo-Web-con-Reflex
```

---

# ⚙️ Instalación con Poetry

## Instalar dependencias

```bash id="n7x58n"
poetry install
```

---

# 🧪 Activar entorno virtual

```bash id="tkwjrz"
poetry shell
```

Si no funciona:

```bash id="mhv4nv"
poetry env activate
```

---

# ▶️ Ejecutar el proyecto

```bash id="3p7u67"
poetry run reflex run
```

Abrir en:

```text id="9ovh52"
http://localhost:3000
```

---

# 🏗️ Build producción

```bash id="q7o3xr"
poetry run reflex export
```

---

# ✨ Funcionalidades

## ✅ Navbar

* Menú responsive
* Logo
* Íconos
* CTA button

---

## ✅ Hero Section

* Imagen principal
* Texto promocional
* Botón “Shop Now”
* Diseño pastel elegante

---

## ✅ Featured Products

* Cards responsive
* Imagen de producto
* Precio
* Nombre
* Categoría

---

## ✅ Promotional Banner

Banner promocional tipo:

```text id="m8xptg"
Spring Beauty Sale
Up to 40% Off
```

---

## ✅ Beauty Categories

Grid de categorías beauty:

* Facial Care
* Makeup
* Skin Care
* Cosmetics

---

## ✅ Footer

* Redes sociales
* Navegación
* Contacto

---

# 🎨 Diseño UI

## Paleta de colores

```python id="d0r0ql"
PRIMARY = "#E7B8B5"
BACKGROUND = "#F8EEEE"
TEXT = "#1A1A1A"
MUTED = "#777777"
```

---

## Tipografías

### Headings

* Syne

### Body

* DM Sans

---

# 📱 Responsive Design

Compatible con:

* Mobile
* Tablet
* Desktop

Usando responsive props de Reflex:

```python id="wb0xj0"
width=["100%", "50%", "25%"]
```

---

# 📄 pyproject.toml

```toml id="ys0n4k"
[tool.poetry]
name = "desarrollo-web-con-reflex"
version = "0.1.0"
description = "Beauty cosmetics clone with Reflex"
authors = ["Lorena Dreyes"]

[tool.poetry.dependencies]
python = "^3.10"
reflex = "*"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

# ⚠️ Errores comunes

| Error                         | Solución                   |
| ----------------------------- | -------------------------- |
| `ModuleNotFoundError`         | Ejecutar `poetry install`  |
| `Node version incompatible`   | Instalar Node.js 18+       |
| `Invalid var passed for prop` | Revisar tipos de datos     |
| `Frontend failed to compile`  | Reiniciar con `reflex run` |

---

# 📚 Recursos

* [Reflex Documentation](https://reflex.dev/docs/getting-started/introduction/?utm_source=chatgpt.com)
* [Poetry Documentation](https://python-poetry.org/docs/?utm_source=chatgpt.com)
* [Google Fonts — Syne](https://fonts.google.com/specimen/Syne?utm_source=chatgpt.com)
* [Google Fonts — DM Sans](https://fonts.google.com/specimen/DM+Sans?utm_source=chatgpt.com)

---

# 📌 Notas

Este proyecto:

* es únicamente educativo
* recrea una UI de referencia
* no incluye backend ecommerce real
* no procesa pagos
* no está afiliado a ninguna marca

---

# 🧠 Objetivo del proyecto

Practicar:

* Reflex
* Poetry
* Responsive Design
* UI moderna ecommerce
* Componentes reutilizables
* Frontend con Python
* Arquitectura web moderna
