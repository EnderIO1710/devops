import psutil
import time
from tabulate import tabulate

def get_cpu_usage():
  
  return psutil.cpu_percent(interval=1)

def get_memory():
  memory = psutil.virtual_memory()

  return {
    'mMax': f"{memory.total / (1024**3):.2f} ГБ",
    'mUsed': f"{memory.used / (1024**3):.2f} ГБ",
    'mAvail': f"{memory.available / (1024**3):.2f} ГБ",
    'mPercent': f"{memory.percent}%"
  }


def get_disk_usage():
  disk = psutil.disk_usage('C:')

  return {
    'dMax': f"{disk.total / (1024**3):.2f} ГБ",
    'dUsed': f"{disk.used / (1024**3):.2f} ГБ",
    'dAvail': f"{disk.free / (1024**3):.2f} ГБ",
    'dPercent': f"{disk.percent}%"
  }

def get_top_processes_mem(n=5):
  
  _ = list(psutil.process_iter())
  time.sleep(1)

  processes = list()

  for proc in sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']), key=lambda procObj: procObj.info['memory_percent'], reverse=True)[:n]:
    try:
      processes.append([
        proc.info['pid'], 
        proc.info['name'], 
        f"{proc.info['cpu_percent']:.2f}%", 
        f"{proc.info['memory_percent']:.2f}%"
      ])
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
      pass

  return processes


def main():
  print("=== Мониторинг системы ===")
   
  print(f"\nЗагрузка CPU: {get_cpu_usage()}%")

  # Общее использование памяти (свободная и используемая, включая проценты)
  print('\nИспользовано памяти')
  for key, value in get_memory().items():
    print(f"{key}: {value}")

  # Общее использование диска (свободно и занято, включая процент)
  print('\nИспользовано диского пространства')
  for key, value in get_disk_usage().items():
    print(f"{key}: {value}")

  # Пять самых загруженных процессов по загрузке ЦП
  print("\nТоп процессов по использованию CPU:")
  top_processes = get_top_processes_mem()

  print(tabulate(top_processes, 
                   headers=['PID', 'Название', 'CPU %', 'Память %'], 
                   tablefmt='grid'))


if __name__ == '__main__':
  main()


