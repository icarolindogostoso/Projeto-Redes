try:
    import wmi

    w = wmi.WMI(namespace="root\\wmi")
    temperatures = w.MSAcpi_ThermalZoneTemperature()
    if temperatures:
        print((temperatures[0].CurrentTemperature / 10.0) - 273.15)
except Exception as e:
    print(e)