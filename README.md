# Integrador_Inventario_ferreteria

flowchart TD
    A([Inicio de Programa]) --> B[inventario = lista vacía]
    B --> C{Menú Principal}
    
    C -->|Opción 1 y 5| D[Módulo: Alta de Producto]
    D --> D1{¿Nombre vacío o duplicado?}
    D1 -->|Sí| D2[ValueError: Solicitar de nuevo] --> D1
    D1 -->|No| D3{¿Stock válido e int >= 0?}
    D3 -->|No| D4[ValueError: Solicitar de nuevo] --> D3
    D3 -->|Sí| D5[Anexar diccionario a lista] --> C
    
    C -->|Opción 2, 3, 4 y 6| E{¿Inventario vacío?}
    E -->|Sí| F[Aviso: No hay stock] --> C
    
    E -->|No / Opc 2| G[Mostrar todo el inventario] --> C
    E -->|No / Opc 4| H[Filtrar e imprimir cantidad == 0] --> C
    
    E -->|No / Opc 3| I[Buscar por nombre]
    I --> J{¿Existe?}
    J -->|Sí| K[Mostrar cantidad] --> C
    J -->|No| L[Aviso: No encontrado] --> C
    
    E -->|No / Opc 6| M[Buscar producto a actualizar]
    M --> N{¿Existe?}
    N -->|No| L
    N -->|Sí| O[Solicitar nuevo stock]
    O --> P{¿Stock válido >= 0?}
    P -->|No| Q[Capturar Error y cancelar] --> C
    P -->|Sí| R[Actualizar clave 'cantidad'] --> C
    
    C -->|Opción 7| S([Fin / Break])
    C -->|Opción inválida| T[Aviso: Opción incorrecta] --> C
