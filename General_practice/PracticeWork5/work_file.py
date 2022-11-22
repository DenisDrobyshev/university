def file_to_list(name):
    try:
        global file
        file = open(name)
        k = int(file.readline())
        lists = file.read().splitlines()
        lens = len(lists)
        if (lens > k) or (lens == 0) or (lens < k):
            raise Exception('Вы ввели слишком много/мало символом или не ввели вовсе')
        else:
            lists = [int(lists[i]) for i in range(0, k)]
        return lists
    except FileNotFoundError:
        return 'Файл не найден'
    except ValueError:
        return 'Недопустимое значение для первой строчки'
    except Exception as ex:
        return f'Ошибка обработки: {str(ex)}'
    finally:
        try:
            file.close()
        except NameError:
            print('Неверное название')
        except Exception as ex:
            print(ex)
            pass

print(file_to_list('text2.txt'))