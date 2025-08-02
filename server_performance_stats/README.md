# Статистика производительности сервера
скрипт для анализа базовой статистики производительности сервера.

## Результат работы
Выводит в CLI информацию о:
- Общая загрузка CPU
- Информацию о ОЗУ: Максимальная, использовано, свободно, занято в %
- Информацию дисковом пространстве: Максимальная, использовано, свободно, занято в %
- Топ 5 процессов отсортированных по ОЗУ

## Getting Started for python-script
1. **Клонировать репозисторий**
    ```
    git clone https://github.com/EnderIO1710/devops.git .
    ```

2. **Установите зависимости**
    ```
    python pip install -r req.txt
    ```

3. **Запуск**  
    ```
    cd server_performance_stats
    python server_stat.py
    ```

## Getting Started for bash-script
1. **Клонировать репозисторий**
    ```
    git clone https://github.com/EnderIO1710/devops.git .
    cd server_performance_stats
    ```
2. **Сделать скрипт исполняемым**
    ```
    chmod +x server_stat.sh
    ```
3. **Запуск**  
    ```
    bash ./server_stat.sh
    ```
