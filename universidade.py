# -*- coding: utf-8 -*-

import asyncio
import os.path

lista_matriculas = []
async def buscar_alunos_formandos(nome_do_curso):
    lista_formandos = []
    global lista_matriculas
    with open(f"cursos/{nome_do_curso}", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split()
            if len(partes) >= 4:
                matricula = partes[0]
                status = partes[3]
                if status == 'CONCLUIDO':
                    if matricula not in lista_matriculas:
                        lista_formandos.append(linha)
                        print()
                    else:
                        lista_matriculas.append(matricula)
    lista_sem_duplicados = list(set(lista_formandos))
    print(*lista_sem_duplicados, sep='\n')

async def get_filenames():
    return [filename for filename in os.listdir("cursos") if os.path.isfile(f"cursos/{filename}")]

async def main():
    filenames = await get_filenames()
    tasks = []
    for filename in filenames:
        task = asyncio.create_task(buscar_alunos_formandos(filename))
        tasks.append(task)

    await asyncio.gather(*tasks)


