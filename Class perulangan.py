class Perulangan:
  """Kelas untuk membuat berbagai jenis perulangan."""

  def __init__(self, start, stop, step=1):
    """Inisialisasi objek Perulangan.

    Args:
      start: Nilai awal perulangan.
      stop: Nilai akhir perulangan.
      step: Nilai langkah perulangan (default 1).
    """
    self.start = start
    self.stop = stop
    self.step = step

  def for_loop(self):
    """Melakukan perulangan for."""
    for i in range(self.start, self.stop, self.step):
      print(i)

  def while_loop(self):
    """Melakukan perulangan while."""
    i = self.start
    while i < self.stop:
      print(i)
      i += self.step

  def for_loop_custom(self, iterable):
    """Melakukan perulangan for dengan iterable custom."""
    for item in iterable:
      print(item)

# Contoh penggunaan
perulangan1 = Perulangan(1, 10)
perulangan1.for_loop()  # Output: 1 2 3 4 5 6 7 8 9

perulangan2 = Perulangan(0, 10, 2)
perulangan2.for_loop()  # Output: 0 2 4 6 8

perulangan3 = Perulangan(10, 0, -1)
perulangan3.while_loop()  # Output: 10 9 8 7 6 5 4 3 2 1

daftar_angka = [1, 5, 10, 15, 20]
perulangan4 = Perulangan(0, len(daftar_angka))
perulangan4.for_loop_custom(daftar_angka)  # Output: 1 5 10 15 20
