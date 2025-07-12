# FastInventory

FastInventory es una API REST moderna y eficiente desarrollada con **FastAPI** para la gestión completa de inventarios de productos. La aplicación permite administrar productos y categorías mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar) con una base de datos PostgreSQL.

## 🚀 Características Principales

- **API REST completa** con documentación automática (Swagger/OpenAPI)
- **Gestión de productos** con SKU único, nombre, precio y categoría
- **Gestión de categorías** para organizar productos
- **Base de datos PostgreSQL** con SQLAlchemy ORM
- **Validación automática** de datos con Pydantic
- **Manejo de errores** robusto y respuestas HTTP apropiadas
- **Relaciones entre entidades** (productos pertenecen a categorías)

## 📋 Requisitos Previos

- **Python 3.8** o superior
- **PostgreSQL** instalado y configurado
- [Visual Studio Code](https://code.visualstudio.com/) (opcional, pero recomendado)

## 🏗️ Estructura del Proyecto

```
FastInventory/
├── app.py                 # Punto de entrada de la aplicación
├── requirements.txt       # Dependencias del proyecto
├── database/             # Configuración de base de datos
├── models/               # Modelos de SQLAlchemy
│   ├── product.py       # Modelo de Producto
│   └── category.py      # Modelo de Categoría
├── routes/              # Endpoints de la API
│   ├── product.py       # Rutas de productos
│   └── category.py      # Rutas de categorías
└── schemas/             # Esquemas Pydantic
    ├── product.py       # Esquemas de Producto
    └── category.py      # Esquemas de Categoría
```

## 🛠️ Configuración del Entorno Virtual

Para aislar las dependencias del proyecto, se recomienda utilizar un entorno virtual:

1. **Abra una terminal** en la raíz del proyecto
2. **Cree el entorno virtual**:

   ```powershell
   python -m venv venv
   ```

3. **Active el entorno virtual**:

   ```powershell
   .\venv\Scripts\Activate
   ```

   > **Nota:** Si utiliza una terminal diferente, el comando de activación puede variar.

## 📦 Instalación de Dependencias

Con el entorno virtual activado, instale las dependencias necesarias:

```powershell
pip install -r requirements.txt
```

### Principales Dependencias

- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para base de datos
- **psycopg2**: Driver de PostgreSQL
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI

## 🗄️ Configuración de Base de Datos

1. **Instale PostgreSQL** en su sistema
2. **Cree una base de datos** para el proyecto
3. **Configure las variables de entorno** (opcional):
   - `DATABASE_URL`: URL de conexión a PostgreSQL

## 🚀 Ejecución del Proyecto

Para iniciar el servidor de desarrollo:

```powershell
uvicorn app:app --host=localhost --port=8000 --reload
```

Una vez iniciado, la documentación interactiva estará disponible en:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📚 Endpoints Disponibles

### Productos (`/products`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/products` | Obtener todos los productos |
| `POST` | `/product` | Crear un nuevo producto |
| `PUT` | `/product/{sku}` | Actualizar un producto existente |
| `DELETE` | `/product/{sku}` | Eliminar un producto |

### Categorías (`/categories`)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/categories` | Obtener todas las categorías |
| `POST` | `/category` | Crear una nueva categoría |
| `PUT` | `/category/{id}` | Actualizar una categoría existente |
| `DELETE` | `/category/{id}` | Eliminar una categoría |

## 📊 Modelos de Datos

### Producto
- **sku** (String, 3 caracteres): Identificador único del producto
- **name** (String, 75 caracteres): Nombre del producto
- **price** (Float): Precio del producto
- **category_id** (Integer): ID de la categoría asociada

### Categoría
- **id** (Integer): Identificador único de la categoría
- **name** (String, 75 caracteres): Nombre de la categoría

## 🔧 Funcionalidades

- **Validación automática** de datos de entrada
- **Manejo de errores** con códigos HTTP apropiados
- **Relaciones entre entidades** (productos-categorías)
- **Prevención de duplicados** (SKU único, nombres únicos)
- **Integridad referencial** (no se pueden eliminar categorías con productos)

## 📖 Documentación Adicional

- [Documentación de FastAPI](https://fastapi.tiangolo.com/es/)
- [Documentación de SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentación de Uvicorn](https://www.uvicorn.org/)

---

**FastInventory** - Gestión eficiente de inventarios con FastAPI
