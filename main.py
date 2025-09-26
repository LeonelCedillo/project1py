from transaction import Type, Transaction


tran1 = Transaction("1/3/2025", Type.DEBIT.value, "Withdrawal @ ATMGO8 111 E SHAW etc", -400, 7681.28)


print(tran1)
