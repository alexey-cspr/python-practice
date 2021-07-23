import tempfile
import os
import asyncio
from aiofile import async_open

def merge_files(files_list, data_output_file):
    for (tmpfile_1, tmpfile_2) in zip(files_list[::2], files_list[1::2]):
        temp_1 = tmpfile_1.readline()
        temp_2 = tmpfile_2.readline()
        temp_file = tempfile.TemporaryFile("w+t")
        while temp_1 != "" or temp_2 != "":
            if not temp_1 and temp_2:
                temp_file.write(temp_2)
                temp_2 = tmpfile_2.readline()
            elif temp_1 and not temp_2:
                temp_file.write(temp_1)
                temp_1 = tmpfile_1.readline()
            elif int(temp_1) >= int(temp_2):
                temp_file.write(temp_2)
                temp_2 = tmpfile_2.readline()
            elif int(temp_1) < int(temp_2):
                temp_file.write(temp_1)
                temp_1 = tmpfile_1.readline()
        temp_file.seek(0)
        i = files_list.index(tmpfile_1)
        files_list[i].close()
        files_list[i + 1].close()
        files_list[i:i + 2] = [temp_file]
    if len(files_list) > 1:
        merge_files(files_list, data_output_file)
    else:
        with open(data_output_file, "w") as result:
            answ = files_list[0].readlines()
            result.writelines(answ)
            files_list[0].close()

def to_tmp(values, files_list):
    temp_file = tempfile.TemporaryFile("w+t")
    for num in map(str, values):
        temp_file.write(num + "\n")
    temp_file.seek(0)
    files_list.append(temp_file)
    values.clear()

async def ex_sort(data_input_file, data_output_file, len):
    with open(data_input_file) as file:
        files_list = []
        values = []
        count = 0
        num = file.readline()
        while num != "":
            values.append(int(num))
            count += 1
            if count % len == 0:
                values.sort()
                to_tmp(values, files_list)
                count = 0
            num = file.readline()
        values.sort()
        to_tmp(values, files_list)
        merge_files(files_list, data_output_file)


async def main():
    await sort(f'{os.getcwd()}\\input1', f'{os.getcwd()}\\output1', 10)
    await sort(f'{os.getcwd()}\\input2', f'{os.getcwd()}\\output2', 100)
    await sort(f'{os.getcwd()}\\input3', f'{os.getcwd()}\\output3', 1000)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())