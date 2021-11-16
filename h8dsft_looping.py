# FTDS // NG- 1

nas = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 
     47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949]
    
for angkagenap in nas :             # Untuk angkagenap di dalam list nas
    if angkagenap % 2 == 0 :        # Menghasilkan angka genap
        if angkagenap == 918:       # Setelah menghasilkan angka genap, perhitungan akan berhenti ketika mencapai bilangan 918
            break                   # Instruksi break untuk menghentikan perhitungan
        print(angkagenap)           # Menampilkan output dari angkagenap
print("Done")                       # Menampilkan pesan "Done"