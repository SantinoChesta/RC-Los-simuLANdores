import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

A_m = 5
f_m = 4000
A_p = 5
f_p = 40000
ka = 3

PERIODOS = 5
MAX_PUNTOS = 20000


def crear_tiempo(f_m, f_p):
    t_final = PERIODOS / f_m
    n = int(min(round(t_final * 10 * f_p), MAX_PUNTOS))
    t = np.linspace(0, t_final, n, endpoint=False)
    return t, t_final, n


def generar(t, A_m, f_m, A_p, f_p, ka):
    moduladora = A_m * np.cos(2 * np.pi * f_m * t)
    portadora = A_p * np.cos(2 * np.pi * f_p * t)
    am = A_p * (1 + ka * np.cos(2 * np.pi * f_m * t)) * np.cos(2 * np.pi * f_p * t)
    return moduladora, portadora, am


def espectro(signal, n, t_final):
    fs = n / t_final
    freqs = np.fft.rfftfreq(n, d=1 / fs)
    mag = np.abs(np.fft.rfft(signal)) * 2 / n
    return freqs / 1000, mag, fs


def envolver(texto, ancho=42):
    lineas = []
    for parrafo in texto.split('\n'):
        linea = ''
        for palabra in parrafo.split(' '):
            if linea and len(linea) + 1 + len(palabra) > ancho:
                lineas.append(linea)
                linea = palabra
            else:
                linea = (linea + ' ' + palabra).strip()
        lineas.append(linea)
    return '\n'.join(lineas)


fig = plt.figure(figsize=(11, 10))
plt.subplots_adjust(left=0.08, right=0.96, top=0.96, bottom=0.30)

ax_mod = fig.add_subplot(4, 1, 1)
ax_por = fig.add_subplot(4, 1, 2)
ax_am = fig.add_subplot(4, 1, 3)
ax_esp = fig.add_subplot(4, 1, 4)

t, t_final, n = crear_tiempo(f_m, f_p)
moduladora, portadora, am = generar(t, A_m, f_m, A_p, f_p, ka)

line_mod, = ax_mod.plot(t, moduladora, 'g')
line_por, = ax_por.plot(t, portadora, 'r')
line_am, = ax_am.plot(t, am, 'purple')

freqs, mag, fs = espectro(am, n, t_final)
line_esp, = ax_esp.plot(freqs, mag, 'b')
line_lsb, = ax_esp.plot([], [], 'g--', linewidth=1.2, label='Bandas laterales (fp±fm)')
line_usb, = ax_esp.plot([], [], 'g--', linewidth=1.2)
line_car, = ax_esp.plot([], [], 'r--', linewidth=1.2, label='Portadora (fp)')

ax_mod.set_title('Señal de Mensaje o Moduladora')
ax_mod.set_ylabel('Amplitud')
ax_por.set_title('Señal Portadora')
ax_por.set_ylabel('Amplitud')
ax_am.set_title('Modulación AM')
ax_am.set_ylabel('Amplitud')
ax_am.set_xlabel('Tiempo (s)')
ax_esp.set_title('Espectro en frecuencia (FFT)')
ax_esp.set_ylabel('Amplitud')
ax_esp.set_xlabel('Frecuencia (kHz)')
ax_esp.grid(True, alpha=0.3)
ax_esp.legend(loc='upper right', fontsize=8)

display_text = fig.text(0.70, 0.115, '', ha='center', va='center', fontsize=10.5,
                        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

ax_sl = [
    fig.add_axes([0.15, y, 0.33, 0.03])
    for y in (0.02, 0.065, 0.11, 0.155, 0.20)
]

sl_A_m = Slider(ax_sl[0], 'A_m (moduladora)', 0.1, 10.0, valinit=A_m, valfmt='%.2f')
sl_A_p = Slider(ax_sl[1], 'A_p (portadora)', 0.1, 10.0, valinit=A_p, valfmt='%.2f')
sl_f_m = Slider(ax_sl[2], 'f_m (Hz)', np.log10(100), np.log10(10000),
                valinit=np.log10(f_m), valfmt=lambda v: f'{10 ** v:,.0f}')
sl_f_p = Slider(ax_sl[3], 'f_p (Hz)', np.log10(1000), np.log10(100000),
                valinit=np.log10(f_p), valfmt=lambda v: f'{10 ** v:,.0f}')
sl_ka = Slider(ax_sl[4], 'ka (índice)', 0.0, 5.0, valinit=ka, valstep=0.05, valfmt='%.2f')


def update(_):
    A_m_v = sl_A_m.val
    A_p_v = sl_A_p.val
    f_m_v = 10 ** sl_f_m.val
    f_p_v = 10 ** sl_f_p.val
    ka_v = sl_ka.val

    t, t_final, n = crear_tiempo(f_m_v, f_p_v)
    moduladora, portadora, am = generar(t, A_m_v, f_m_v, A_p_v, f_p_v, ka_v)

    line_mod.set_data(t, moduladora)
    line_por.set_data(t, portadora)
    line_am.set_data(t, am)

    ax_mod.set_xlim(t[0], t[-1])
    ax_por.set_xlim(t[0], t[-1])
    ax_am.set_xlim(t[0], t[-1])
    ax_mod.set_ylim(-1.1 * A_m_v, 1.1 * A_m_v)
    ax_por.set_ylim(-1.1 * A_p_v, 1.1 * A_p_v)
    ax_am.set_ylim(-1.1 * A_p_v * (1 + ka_v), 1.1 * A_p_v * (1 + ka_v))

    freqs, mag, fs = espectro(am, n, t_final)
    y_top = max(mag.max(), 1e-12) * 1.2
    line_esp.set_data(freqs, mag)
    ax_esp.set_xlim(0, (f_p_v + 2 * f_m_v) / 1000)
    ax_esp.set_ylim(0, y_top)

    line_lsb.set_data([(f_p_v - f_m_v) / 1000] * 2, [0, y_top])
    line_usb.set_data([(f_p_v + f_m_v) / 1000] * 2, [0, y_top])
    line_car.set_data([f_p_v / 1000] * 2, [0, y_top])

    if ka_v < 1:
        estado = 'Submodulación (ka < 1): la envolvente no llega a cero'
    elif ka_v == 1:
        estado = 'Modulación al 100 % (ka = 1): la envolvente toca cero'
    else:
        estado = 'SOBREMODULACIÓN (ka > 1): envolvente distorsionada'
    if f_p_v <= f_m_v:
        estado += '  |  ⚠ la portadora debe tener mayor frecuencia que la moduladora'
    elif fs < 10 * f_p_v:
        estado += '  |  ⚠ fs < 10·fp: posible alias en el gráfico'

    display_text.set_text(envolver(
        f'AM(t) = Ap·[1 + ka·cos(2π·fm·t)]·cos(2π·fp·t)\n'
        f'Ap={A_p_v:.2f}   fp={f_p_v / 1000:.1f} kHz   fm={f_m_v / 1000:.2f} kHz   ka={ka_v:.2f}\n'
        f'{estado}'
    ))
    display_text.set_color('red' if ka_v > 1 else 'black')
    fig.canvas.draw_idle()


for sl in (sl_A_m, sl_A_p, sl_f_m, sl_f_p, sl_ka):
    sl.on_changed(update)

update(None)

print('''
Modulación AM interactiva
--------------------------
Usá los sliders de abajo para variar los parámetros y ver cómo cambian las señales:

  A_m — amplitud de la señal moduladora (0.1–10)
  A_p — amplitud de la señal portadora (0.1–10)
  f_m — frecuencia de la moduladora, escala logarítmica (100 Hz – 10 kHz)
  f_p — frecuencia de la portadora, escala logarítmica (1 kHz – 100 kHz)
  ka  — índice de modulación (0–5); ka > 1 produce sobremodulación

El 4to gráfico muestra el espectro en frecuencia: la portadora en fp y las
bandas laterales en fp±fm. El ancho de banda total es BW = 2·fm.
''')

plt.show()