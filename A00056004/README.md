# Sistemas Operacionales - Parcial 3
**Nombre:** Brayan Andrés Henao  
**Código:** A00056004  
**Correo:** bryanhenao96@gmail.com  
**URL Repositorio:** https://github.com/brayanhenao/so-exam3
___

## 4) Servicio web con Flask

Para la creación de un servicio web con flask, se utilizan como base los archivos presentes en el repositorio so-microservices[](), taller realizado en clase para la creación de microservicios.

Para los requerimientos del parcial, se requiere además de saber el porcentaje actual de la CPU, obtener la memoria RAM utilizada y el espacio en el disco duro disponible, para esto al archivo op_stats/stats.py se le agregan estos dos últimos métodos:

```python
import psutil

class Stats():

  @classmethod
  def get_cpu_percent(cls):
    cpu_percent = psutil.cpu_percent()
    return cpu_percent
	
  @classmethod
  def get_ram(cls):
    memory = psutil.virtual_memory();
    available = memory[1]
    return available
  
  @classmethod
  def get_free_disk(cls):
    disk = psutil.disk_usage('/')
	freedisk = disk[2]
    return freedisk
```

Para exponer los servicios mediante Flask, se modifica el archivo op_stats/app.py en donde se agregan los dos nuevos servicios a exponer:
