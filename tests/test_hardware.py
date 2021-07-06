from unittest import TestCase,main

from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class TestHardware(TestCase):
    def setUp(self) -> None:
        self.hardware =Hardware("My name", "Heavy", 500,500)

    def test_attr_are_set(self):
        self.assertEqual("My name", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(500, self.hardware.capacity)
        self.assertEqual(500, self.hardware.memory)
        self.assertEqual([],self.hardware.software_components)

    def test_hardware_has_no_memory_when_software_is_installed_raises(self):
        software = LightSoftware("S software", 501,501)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_install_hardware_equal_software_is_installed(self):
        software = LightSoftware("S software", 200,1000)

        self.hardware.install(software)
        self.assertEqual(1,len(self.hardware.software_components))

    def test_install_hardware_software_is_installed(self):
        software = LightSoftware("S software", 200,500)

        self.hardware.install(software)
        self.assertEqual(1,len(self.hardware.software_components))

    def test_uninstall_hardware_software_is_installed_when_installed_before(self):
        software = LightSoftware("S software", 200,500)

        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))
        self.hardware.uninstall(software)
        self.assertEqual(0,len(self.hardware.software_components))

    def test_uninstall_hardware_software_is_installed_when_no_software(self):
        software = LightSoftware("S software", 200,500)
        software1 = LightSoftware("S1 software", 1,2)
        self.hardware.install(software)
        self.assertIn(software, self.hardware.software_components)
        self.assertNotIn(software1, self.hardware.software_components)
        self.hardware.uninstall(software1)

        self.assertEqual(1,len(self.hardware.software_components))

if __name__=="__main__":
    main()