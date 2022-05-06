from conta import ContaCorrente

conta1 = ContaCorrente(123, 'Athos', 150, 1000)
conta2 = ContaCorrente(321, 'Karol', 50, 1000)
conta3 = ContaCorrente(1010, 'Juca', 60, 1000)

print(conta1.extrato())
