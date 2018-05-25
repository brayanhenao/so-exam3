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
	free_disk = disk[2]
    return free_disk
