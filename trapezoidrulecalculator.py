import numpy as np
import matplotlib.pyplot as plt

def trapezoid_rule(f, a, b, n):
    """
    Implementasi Aturan Trapezoid untuk integrasi numerik

    Parameters:
    f : fungsi yang akan diintegralkan
    a : batas bawah integral
    b : batas atas integral
    (catatan untuk batas integral : misalkan jika kalian ingin menginput 2pi/5
    maka tulislah dengan oprasi perkalian seperti ini -> 2*pi/5)
    n : jumlah subinterval (partisi)

    Returns:
    integral : nilai aproksimasi integral
    """
    # Hitung lebar setiap subinterval
    h = (b - a) / n

    # Hitung nilai fungsi di titik-titik
    x = np.linspace(a, b, n+1)
    y = f(x)

    # Rumus Trapezoid: I ≈ h/2 * [f(x0) + 2*f(x1) + 2*f(x2) + ... + 2*f(xn-1) + f(xn)]
    integral = (h/2) * (y[0] + 2*np.sum(y[1:-1]) + y[-1])

    return integral, x, y

def parse_function(func_str):
    """
    Mengubah string fungsi menjadi fungsi Python yang bisa dievaluasi
    """
    # Ganti notasi matematika umum dengan numpy
    func_str = func_str.replace('^', '**')
    func_str = func_str.replace('sin', 'np.sin')
    func_str = func_str.replace('cos', 'np.cos')
    func_str = func_str.replace('tan', 'np.tan')
    func_str = func_str.replace('exp', 'np.exp')
    func_str = func_str.replace('log', 'np.log')
    func_str = func_str.replace('sqrt', 'np.sqrt')
    func_str = func_str.replace('pi', 'np.pi')
    func_str = func_str.replace('e', 'np.e')

    # Buat fungsi lambda
    return lambda x: eval(func_str)

# Fungsi bantu untuk parsing input numerik
def parse_numeric_input(input_str):
    input_str = input_str.replace('pi', 'np.pi')
    input_str = input_str.replace('e', 'np.e')
    return float(eval(input_str))

# ===== PROGRAM INTERAKTIF =====

print("=" * 70)
print("KALKULATOR INTEGRAL ATURAN TRAPEZOID - VERSI INTERAKTIF")
print("=" * 70)
print("\nPetunjuk penulisan fungsi:")
print("  - Gunakan 'x' sebagai variabel")
print("  - Pangkat: x**2 atau x^2")
print("  - Fungsi trigonometri: sin(x), cos(x), tan(x)")
print("  - Eksponensial: exp(x)")
print("  - Logaritma natural: log(x)")
print("  - Akar: sqrt(x)")
print("  - Konstanta: pi, e")
print("\nContoh fungsi:")
print("  - x**2 + 3*x + 1")
print("  - sin(x) + cos(x)")
print("  - exp(-x**2)")
print("  - 1/x")
print("  - sqrt(x)")
print("=" * 70)

try:
    # Input fungsi
    print("\n[1] MASUKKAN FUNGSI")
    print("-" * 70)
    func_input = input("Masukkan fungsi f(x): ")

    # Parse fungsi
    f = parse_function(func_input)

    # Input batas integral
    print("\n[2] MASUKKAN BATAS INTEGRAL")
    print("-" * 70)
    a_str = input("Batas bawah (a): ")
    b_str = input("Batas atas (b): ")

    a = parse_numeric_input(a_str)
    b = parse_numeric_input(b_str)

    if a >= b:
        print("\nERROR: Batas bawah harus lebih kecil dari batas atas!")
        exit()

    # Input jumlah subinterval
    print("\n[3] MASUKKAN JUMLAH SUBINTERVAL")
    print("-" * 70)
    n = int(input("Jumlah subinterval (n): "))

    if n <= 0:
        print("\nERROR: Jumlah subinterval harus positif!")
        exit()

    # Input nilai eksak (opsional)
    print("\n[4] NILAI EKSAK (OPSIONAL)")
    print("-" * 70)
    eksak_input = input("Nilai eksak integral (tekan Enter jika tidak tahu): ")

    nilai_eksak = None
    if eksak_input.strip():
        try:
            nilai_eksak = parse_numeric_input(eksak_input)
        except:
            print("Nilai eksak tidak valid, akan diabaikan.")

    # Hitung integral
    print("\n" + "=" * 70)
    print("HASIL PERHITUNGAN")
    print("=" * 70)

    hasil, x_points, y_points = trapezoid_rule(f, a, b, n)

    print(f"\nFungsi: f(x) = {func_input}")
    print(f"Interval: [{a}, {b}]")
    print(f"Jumlah subinterval: {n}")
    print(f"Lebar subinterval (h): {(b-a)/n:.6f}")
    print(f"\n{'='*70}")
    print(f"HASIL INTEGRAL: {hasil:.10f}")
    print(f"{'='*70}")

    if nilai_eksak is not None:
        error = abs(nilai_eksak - hasil)
        error_persen = (error/abs(nilai_eksak)) * 100 if nilai_eksak != 0 else 0
        print(f"\nNilai eksak: {nilai_eksak:.10f}")
        print(f"Error absolut: {error:.10f}")
        print(f"Error relatif: {error_persen:.4f}%")

    # Tampilkan tabel perhitungan
    print("\n" + "=" * 70)
    print("TABEL PERHITUNGAN")
    print("=" * 70)
    print(f"{'i':>4} | {'x_i':>12} | {'f(x_i)':>15} | {'Koefisien':>10} | {'Kontribusi':>15}")
    print("-" * 70)

    h = (b - a) / n
    for i, (xi, yi) in enumerate(zip(x_points, y_points)):
        if i == 0 or i == len(x_points) - 1:
            koef = 1
        else:
            koef = 2
        kontribusi = koef * yi
        print(f"{i:4d} | {xi:12.6f} | {yi:15.6f} | {koef:10d} | {kontribusi:15.6f}")

    print("-" * 70)
    print(f"Integral ≈ (h/2) × Σ = ({h:.6f}/2) × {y_points[0] + 2*np.sum(y_points[1:-1]) + y_points[-1]:.6f}")
    print(f"         = {hasil:.10f}")

    # Tanya apakah ingin visualisasi
    print("\n" + "=" * 70)
    vis = input("\nApakah Anda ingin melihat visualisasi? (y/n): ")

    if vis.lower() == 'y':
        print("\nMembuat visualisasi...")

        # Buat plot
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle(f'Visualisasi Aturan Trapezoid: ∫ ({func_input}) dx dari {a} ke {b}',
                     fontsize=14, fontweight='bold')

        # Plot 1: Trapezoid
        ax = axes[0]
        x_curve = np.linspace(a, b, 500)
        try:
            y_curve = f(x_curve)

            ax.plot(x_curve, y_curve, 'b-', linewidth=2.5, label=f'f(x) = {func_input}')
            ax.plot(x_points, y_points, 'ro-', markersize=8, linewidth=2, label=f'Trapezoid (n={n})')

            # Gambar trapezoid
            for i in range(len(x_points)-1):
                ax.fill_between([x_points[i], x_points[i+1]], 0, [y_points[i], y_points[i+1]],
                                 alpha=0.3, color='yellow', edgecolor='red', linewidth=1.5)

            ax.axhline(y=0, color='k', linewidth=0.5)
            ax.axvline(x=0, color='k', linewidth=0.5)
            ax.grid(True, alpha=0.3)
            ax.set_xlabel('x', fontsize=11)
            ax.set_ylabel('f(x)', fontsize=11)
            ax.set_title(f'Aproksimasi dengan {n} Trapezoid\nHasil: {hasil:.6f}', fontsize=11)
            ax.legend(fontsize=9)
        except:
            ax.text(0.5, 0.5, 'Error: Tidak dapat memplot fungsi',
                   ha='center', va='center', transform=ax.transAxes)

        # Plot 2: Konvergensi (jika nilai eksak diketahui)
        ax = axes[1]
        if nilai_eksak is not None:
            n_values = [1, 2, 4, 8, 16, 32, 64, 128]
            errors = []

            for ni in n_values:
                try:
                    hasil_i, _, _ = trapezoid_rule(f, a, b, ni)
                    error_i = abs(nilai_eksak - hasil_i)
                    errors.append(error_i)
                except:
                    break

            if errors:
                n_values = n_values[:len(errors)]
                ax.loglog(n_values, errors, 'bo-', linewidth=2, markersize=8)
                ax.axvline(x=n, color='r', linestyle='--', linewidth=2, label=f'n = {n} (pilihan Anda)')
                ax.grid(True, alpha=0.3)
                ax.set_xlabel('Jumlah Subinterval (n)', fontsize=11)
                ax.set_ylabel('Error Absolut (log scale)', fontsize=11)
                ax.set_title('Konvergensi Error vs Jumlah Subinterval', fontsize=11)
                ax.legend(fontsize=9)
        else:
            ax.text(0.5, 0.5, 'Nilai eksak tidak diketahui\nGrafik konvergensi tidak tersedia',
                   ha='center', va='center', transform=ax.transAxes, fontsize=11)
            ax.axis('off')

        plt.tight_layout()
        plt.show()

        print("Visualisasi selesai!")

    print("\n" + "=" * 70)
    print("TERIMA KASIH TELAH MENGGUNAKAN KALKULATOR TRAPEZOID!")
    print("=" * 70)

except ValueError as e:
    print(f"\n  ERROR: Input tidak valid! {e}")
except Exception as e:
    print(f"\n  ERROR: {e}")
    print("Pastikan fungsi yang Anda masukkan valid!")