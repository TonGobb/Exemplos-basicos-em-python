# Conversor de segundos para dia,hora,min e segundos.

Total_seg = (eval(input('Entre com o número de segundos que deseja converter: ')))
Total_d = Total_seg//86400
horas_restantes = Total_seg % 86400
Total_hr = horas_restantes//3600
Seg_restantes = horas_restantes % 3600
Total_min = Seg_restantes//60
Seg_rest_finais = Seg_restantes % 60

print(f'O número total de segundo após conversão para Dia, horas, minutos, segundos representa:'
      f'\n{Total_d} Dia(s), {Total_hr} Hora(s), {Total_min} minutos(s), e {Seg_rest_finais} segundo(s)')
