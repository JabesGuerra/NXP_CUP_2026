🏁 NXP_CUP // Dashboard & Leaderboard
Sistema de transmisión, gestión de tiempos y tabla de posiciones en tiempo real con estética Vaporwave / Arcade para competencias de la NXP Cup.

🚀 Características
Leaderboard Dinámico: Renderizado en tiempo real con animaciones en cascada y desplazamiento automático.

Pantalla de Stream (Fullscreen): Modo transmisión integrado mediante iframe con transiciones fluidas de barrido al presionar la tecla F.

Gestión de Reglas Integrada: Vista dedicada (rules.html) con desglose de puntajes, bonificaciones por tiempo y recolección de monedas.

Panel de Control (Admin): Interfaz para actualización manual de tiempos, sanciones, monedas recogidas y configuración de puntuación.

Sincronización: Comunicación entre ventanas utilizando BroadcastChannel y localStorage.

🛠️ Estructura del Proyecto
Plaintext

        ├── index.html              # Pantalla principal del Leaderboard y Stream
        ├── rules.html              # Vista con las reglas del torneo
        ├── admin.html              # Panel de control del evento
        └── assets/
            ├── coins/              # Iconos de monedas (moneda_amarilla.png, etc.)
            └── logos/              # Logotipos de patrocinadores/escuderías
⚙️ Reglas de Puntuación Defectuosas
Límite de carrera: Máximo 5 vueltas.

Vuelta correcta: +150 pts

Vuelta con giro incorrecto: +75 pts

Moneda Amarilla: +30 pts

Moneda Azul: +10 pts

Moneda Roja: -10 pts

Tiempo < 12.0s: +50 pts (Bono Fast Lap)

🕹️ Teclas rápidas
F: Alternar pantalla completa de la transmisión en vivo / volver al Leaderboard.
