from project.software.software import Software


class Hardware:
    def __init__(self,name:str, type:str, capacity:int, memory:int):
        self.memory = memory
        self.capacity = capacity
        self.type = type
        self.name = name
        self.software_components =[]

    def install(self, software:Software):
        if self.available_memory>=software.memory_consumption and \
                self.available_capacity>=software.capacity_consumption:
            self.software_components.append(software)

        else:
            raise Exception("Software cannot be installed")
    @property
    def available_memory(self):
        return self.memory-sum( [s.memory_consumption for s in self.software_components ])

    @property
    def available_capacity(self):
        return self.capacity-sum( [s.capacity_consumption for s in self.software_components ])


    def uninstall(self,software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
