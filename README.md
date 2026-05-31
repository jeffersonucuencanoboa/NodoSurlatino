![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

# NodoSurlatino

Herramienta CLI para optimizar flujos de trabajo y organización automatizada de archivos en entornos de producción tecnológica del Sur Global.

---

## Descripción

NodoSurlatino es una herramienta desarrollada en Python para automatizar la organización de archivos por extensión, permitiendo mantener estructuras de trabajo limpias, eficientes y escalables.

El proyecto está diseñado para ser ligero, portable y fácil de usar incluso en equipos con recursos limitados.

---

## Features

✅ Organización automática de archivos por extensión  
✅ Interfaz CLI usando argparse  
✅ Modo simulación (`--dry-run`)  
✅ Organización recursiva de carpetas  
✅ Logging de actividad  
✅ Configuración mediante JSON  
✅ Soporte para múltiples extensiones  
✅ Arquitectura modular  
✅ Compatible con Windows 10  
✅ Preparado para integración CI/CD

---

## Roadmap

### Próximas mejoras

- [ ] Interfaz gráfica (GUI)
- [ ] Soporte para Linux
- [ ] Configuración YAML
- [ ] Integración con nube
- [ ] Sistema de plugins
- [ ] Organización inteligente mediante IA
- [ ] Dashboard web
- [ ] Procesamiento de archivos grandes

---

## Instalación

```bash
git clone https://github.com/TU-USUARIO/NodoSurlatino.git
cd NodoSurlatino
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Uso

### Organizar carpeta

```bash
python main.py --path test_folder
```

### Simulación sin mover archivos

```bash
python main.py --path test_folder --dry-run
```

### Organización recursiva

```bash
python main.py --path test_folder --recursive
```

---

## Ejemplo de salida

```bash
[INFO] Escaneando carpeta...
[INFO] Moviendo archivo foto.jpg -> images/
[INFO] Moviendo archivo documento.pdf -> documents/
[INFO] Proceso finalizado
```

---

## Screenshots

### CLI funcionando

![Demo](assets/demo.gif)

---

## Estructura del proyecto

```bash
NodoSurlatino/
│
├── task_automator/
│   ├── core.py
│
├── test_folder/
│
├── .github/
│   └── workflows/
│
├── main.py
├── requirements.txt
├── README.md
└── config.json
```

---

## Contributing

Las contribuciones son bienvenidas.

Pasos:

1. Fork del proyecto
2. Crear branch
3. Commit de cambios
4. Push
5. Crear Pull Request

---

## CI/CD

El proyecto incluye GitHub Actions para validación automática básica.

---

## Licencia

MIT License

---

## Autor

Desarrollado por Noboa.
``
---

# Instalación Paso a Paso

## 1. Clonar el repositorio

```bash
git clone https://github.com/jeffersonucuencanoboa/NodoSurlatino.git