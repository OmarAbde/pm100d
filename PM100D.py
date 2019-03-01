
from usbtmc import *


class PM100D(Instrument,UsbtmcException):
	reset = "*OPC?;*OPC 0"

	def __init__(self, idVendor, idProduct):
		self.usbtmc.Instrument(idVendor,idProduct)
							#   --------------------------------------------------------  #
	# Getting the device IDN
	def get_idn(self):
		self.ask(reset)
		return self.ask("*IDN?")

	# Getting the Sensor IDN
	def get_sensor_idn(self):
		self.ask(reset)
		return self.ask("SYSTem:SENSor:IDN?")

	# Getting the system Date
	def get_date(self):
	        self.ask(reset)
	        return self.ask("SYSTem:DATE?")

	# Setting the system Date
	def set_date(self,y,m,d):
		self.ask(reset)
		self.ask("SYSTem:DATE?;DATE " + y + "," + m + "," + d )

	# Getting the system Time
	def get_time(self):
		self.ask(reset)
		return self.ask("SYSTem:TIME?")

	# Setting the system Time
	def set_time(self,h,m,s):
		self.ask(reset)
		self.ask("SYSTem:TIME? ; " + "TIME " + h + "," + m + "," + s )

	# Getting the device line frequency 50kz/60hz
	def get_frequency(self):
		self.ask(reset)
		return self.ask("SYSTem:LFRequency?")

	# Setting the device line frequency 50kz/60hz
	def set_frequency(self,f):
	        self.ask(reset)
	        self.ask("SYSTem:LFRequency? ; " + "LFRequency " + f )

							#   --------------------------------------------------------  #
	# Getting the Brightness [0 1]
	def get_brightness(self):
	        self.ask(reset)
	        return self.ask("DISP:BRIGhtness?")

	# Setting the Brightness [0 1]
	def set_brightness(self,value):
	    self.ask(reset)
	    self.ask( "DISP:BRIGhtness?;BRIGhtness " + value )

	# Getting the Contrast [0 1]
	def get_contrast(self):
	    self.ask(reset)
	    return self.ask("DISP:CONTrast?")

	# Setting the Contrast [0 1]
	def set_contrast(self,value):
	    self.ask(reset)
	    self.ask("DISP:CONTrast? ; "  + "CONTrast " + value)

							#   --------------------------------------------------------  #
	# Getting the Calibration String
	def get_calib_str(self):
	    self.ask(reset)
	    return self.ask("CALibration:STRing?")

							#   --------------------------------------------------------  #
	# Setting the Sense average rate
	def set_sense_average(self,average):
		self.ask(reset)
		self.ask("AVERage:COUNT? ; " + "COUNT " + average)
	    
	# Getting the Sense average rate
	def get_sense_average(self):
		self.ask(reset)
		return self.ask("AVERage:COUNT?")

							#   --------------------------------------------------------  #
	# Setting the attenuation factor in [-60 60]dB or MAX/MIN/DEF
	def set_attenuation_factor(self,atten):
		self.ask(reset)
		self.ask("CORRection? ; " + ":CORRection " + atten) # "CORRection? ;" + 

	# Getting the attenuation factor wich : (MAX/MIN/DEF or nothing for current)
	def get_attenuation_factor(self,wich):
		self.ask(reset)
		return self.ask("CORRection? " + wich)

	# Perform a Zero Adjustment routine
	def zeroing(self):
		self.ask(reset)
		self.ask("*OPC?; :CORRection:COLLect:ZERO")

	# Abort the Zero Adjustment routine
	def abort_zeroing(self):
		self.ask(reset)
		self.ask("*OPC?; :CORRection:COLLect:ZERO:ABORt")

	# Getting the Zero Adjustment routine state 
	def get_zeroing_state(self):
		self.ask(reset)
		return self.ask("CORRection:COLLect:ZERO:STATe?")

	# Getting the Zero value
	def get_zero_value(self):
		self.ask(reset)
		return self.ask("CORRection:COLLect:ZERO:MAGNitude?")

	# Setting the Beam Diameter in [mm] (MAX/MIN/DEF/value)
	def set_beam_diameter(self,beam):
		self.ask(reset)
		self.ask("CORRection:BEAMdiameter? ; " + ":CORRection:BEAMdiameter " + beam)


	# Getting the Beam Diameter in [mm] wich : (MAX/MIN/DEF or nothing for current)
	def get_beam_diameter(self,wich):
		self.ask(reset)
		print self.ask(":CORRection:BEAMdiameter? " + wich )	

	# Setting the Operation Wavelength in [nm] (MAX/MIN/value)
	def set_wavelength(self,wave):
		self.ask(reset)
		self.ask("CORRection:WAVelength?; " + "WAVelength " + wave)

	# Setting the Operation Wavelength in [nm] wich : (MAX/MIN or nothing for current)
	def get_wavelength(self,wich):
		self.ask(reset)
		return self.ask("CORRection:WAVelength? " + wich)

	# Setting the Photodiode response value in A/W (MAX/MIN/DEF/value)
	def set_photo_resp(self,p_resp):
		self.ask(reset)
		self.ask("CORR:POWer:PDIOde? ; " + ":PDIOde " + p_resp)

	# Getting the Photodiode response value in A/W wich : (MAX/MIN/DEF or nothing for current)
	def get_photo_resp(self,wich):
		self.ask(reset)
		return self.ask("CORR:POWer:PDIOde? " + wich)

	# Setting the Thermopile response value in V/W (MAX/MIN/DEF/value)
	def set_thermopile_resp(self,t_resp):
		self.ask(reset)
		self.ask("CORR:POWer:THERmopile? ; " + "POWer:THERmopile " + t_resp)

	# Getting the Thermopile response value in V/W wich : (MAX/MIN/DEF or nothing for current)
	def get_thermopile_resp(self,wich):
		self.ask(reset)
		return self.ask("CORR:POWer:THERmopile?  " + wich)

	# Setting the Pyro_detector response value in V/J (MAX/MIN/DEF/value)
	def set_pyrodetector_resp(self,py_resp):
		self.ask(reset)
		self.ask("CORR:ENERgy:PYRO? ; " + "ENERgy:PYRO " + py_resp)

	# Getting the Pyro_detector response value in V/J wich : (MAX/MIN/DEF or nothing for current)
	def get_pyrodetector_resp(self,wich):
		self.ask(reset)
		return self.ask("CORR:ENERgy:PYRO? " + wich)

							#   --------------------------------------------------------  #
	# Setting the Auto_ranging ON and OFF (ON/OFF/1/0)  **********
	def set_curr_autorang(self,func):
		self.ask(reset)
		self.ask("*OPC?;" + ":CURRent:RANGe:AUTO " + func)

	# Getting the Auto_ranging (Enable/Disable) (ON/OFF/1/0) 
	def get_curr_autorang(self):
		self.ask(reset)
		return self.ask("CURRent:RANGe:AUTO?")

	# Setting the Current Range in [A] (MAX/MIN/value)
	def set_curr_range(self,value):
		self.ask(reset)
		self.ask("*OPC?;" + "CURRent:RANGe " + value)

	# Getting the Current Range in [A] wich : (MAX/MIN)
	def get_curr_range(self,wich):
		self.ask(reset)
		return self.ask("CURRent:RANGe? " + wich)

	# Setting the Current Delta mode ON and OFF (ON/OFF/1/0)
	def set_curr_delta_mode(self,func):
		self.ask(reset)
		self.ask("*OPC?;" + "CURRent:REFerence:STATe " + func)

	# Getting the Current Delta mode State  (Enable/Disable) (ON/OFF/1/0)
	def get_curr_delta_mode(self):
		self.ask(reset)
		return self.ask("CURRent:REFerence:STATe?")

	# Setting the Current Range in [A] (MAX/MIN/DEF/value)
	def set_curr_delta(self,value):
		self.ask(reset)
		self.ask("*OPC?;" + "CURRent:REFerence " + value)

	# Getting the Current Range in [A] wich : (MAX/MIN/DEF or nothing for current)
	def get_curr_delta(self,wich):
		self.ask(reset)
		return self.ask("CURRent:REFerence? " + wich)

							#   --------------------------------------------------------  #
	# Setting the Energy Range in [J] (MAX/MIN/value)
	def set_energy_range(self,value):
		self.ask(reset)
		self.ask("*OPC?;"+ "ENERgy:RANGe " + value)

	# Getting the Energy Range in [J] wich : (MAX/MIN/DEF or nothing for current)
	def get_energy_range(self,wich):
		self.ask(reset)
		return self.ask("ENERgy:RANGe? " +  wich)

	# Setting the Energy Delta reference in [J] (MAX/MIN/value)
	def set_energy_delta(self,value):
		self.ask(reset)
		self.ask("*OPC?;" + "ENERgy:REFerence " + value)

	# Getting the Energy Delta reference in [J] wich : (MAX/MIN/DEF or nothing for current)
	def get_energy_delta(self,wich):
		self.ask(reset)
		return self.ask("ENERgy:REFerence? " +  wich)

	# Setting the Energy Delta mode ON and OFF (ON/OFF/1/0)
	def set_energy_delta_mode(self,value):
		self.ask(reset)
		self.ask("*OPC?;" + "ENERgy:REFerence:STATe " + value)

	# Getting the Energy Delta mode State  (Enable/Disable) (ON/OFF/1/0)
	def get_energy_delta_mode(self):
		self.ask(reset)
		return self.ask("ENERgy:REFerence:STATe? ")

							#   --------------------------------------------------------  #
	# Getting the Frequency Range wich : (UPP/LOW)
	def get_freq_range(self,wich):
		self.ask(reset)
		return self.ask("FREQuency:RANGe:" + wich + "?")

							#   --------------------------------------------------------  #
	# Setting the Power Auto_ranging ON and OFF (ON/OFF/1/0) ////////
	def set_pow_autorang(self,func):
		self.ask(reset)
		self.ask("*OPC?;" + "POWer:RANGe:AUTO " + func)

	# Getting the Power Auto_ranging (Enable/Disable) (ON/OFF/1/0) ****
	def get_pow_autorang(self):
		self.ask(reset)
		return self.ask("POWer:RANGe:AUTO?")

	# Setting the Power Range in [W] (MAX/MIN/value)
	def set_pow_range(self,value):
		self.ask(reset)
		self.ask("*OPC?;" + "POWer:RANGe " + value)

	# Getting the Power Range in [W] wich : (MAX/MIN)
	def get_pow_range(self,wich):
		self.ask(reset)
		return self.ask("POWer:RANGe? " + wich)

	# Setting the Power Delta mode ON and OFF (ON/OFF/1/0)
	def set_pow_delta_mode(self,func):
		self.ask(reset)
		self.ask("*OPC?;" + "POWer:REFerence:STATe " + func)

	# Getting the Power Delta mode State  (Enable/Disable) (ON/OFF/1/0)
	def get_pow_delta_mode(self):
		self.ask(reset)
		return self.ask("POWer:REFerence:STATe?")

	# Setting the Power Delta Reference in [W] (MAX/MIN/DEF/value)
	def set_pow_delta(self,value):
		self.ask(reset)
		self.ask("*OPC?;" + "POWer:REFerence " + value)

	# Getting the Power Delta Reference in [W] wich : (MAX/MIN/DEF or nothing for current)
	def get_pow_delta(self,wich):
		self.ask(reset)
		return self.ask("POWer:REFerence? " + wich)

	# Setting the Power Unit unit :(W/DBM)
	def set_pow_unit(self,unit):
		self.ask(reset)
		self.ask("*OPC?;" + "POWer:UNIT " + unit)

	# Getting the Power Unit unit :(W/DBM)
	def get_pow_unit(self):
		self.ask(reset)
		return self.ask("POWer:UNIT? ")

							#   --------------------------------------------------------  #
	# Setting the Voltage Auto_ranging ON and OFF (ON/OFF/1/0) ////////
	def set_volt_autorang(self,func):
		self.ask(reset)
		self.ask("*OPC?;" + "VOLTage:RANGe:AUTO " + func)

	# Getting the Voltage Auto_ranging (Enable/Disable) (ON/OFF/1/0) ****
	def get_volt_autorang(self):
		self.ask(reset)
		return self.ask("VOLTage:RANGe:AUTO?")

	# Setting the Voltage Range in [V] (MAX/MIN/value)
	def set_volt_range(self,value):
		self.ask(reset)
		self.ask("*OPC?;" + "VOLTage:RANGe " + value)

	# Getting the Voltage Range in [V] wich : (MAX/MIN)
	def get_volt_range(self,wich):
		self.ask(reset)
		return self.ask("VOLTage:RANGe? " + wich)

	# Setting the Voltage Delta mode ON and OFF (ON/OFF/1/0)
	def set_volt_delta_mode(self,func):
		self.ask(reset)
		self.ask("*OPC?;" + "VOLTage:REFerence:STATe " + func)

	# Getting the Voltage Delta mode State  (Enable/Disable) (ON/OFF/1/0)
	def get_volt_delta_mode(self):
		self.ask(reset)
		return self.ask("VOLTage:REFerence:STATe?")

	# Setting the Voltage Delta Reference in [V] (MAX/MIN/DEF/value)
	def set_volt_delta(self,value):
		self.ask(reset)
		self.ask("*OPC?;" + "VOLTage:REFerence " + value)

	# Getting the Voltage Delta Reference in [V] wich : (MAX/MIN/DEF or nothing for current)
	def get_volt_delta(self,wich):
		self.ask(reset)
		return self.ask("VOLTage:REFerence? " + wich)

							#   --------------------------------------------------------  #
	# Setting the Trigger level in [%] (MAX/MIN/DEF/value)
	def set_trigger(self,value):
		self.ask(reset)
		self.ask("*OPC?;" + "PEAKdetector:THReshold " + value)

	# Getting the Voltage Delta Reference in [%] wich : (MAX/MIN/DEF or nothing for current)
	def get_trigger(self,wich):
		self.ask(reset)
		return self.ask("PEAKdetector:THReshold? " + wich)

							#   --------------------------------------------------------  #
	# Setting the Photodiode Bandwidth input stage ON and OFF  (ON/OFF/1/0)
	def set_pdiode_band(self,mode):
		self.ask(reset)
		self.ask("*OPC?;" + "INPut:PDIode:FILTer:STATe " + mode)

	# Getting the Photodiode Bandwidth input stage (Enable/Disable) (ON/OFF/1/0)
	def get_pdiode_band(self):
		self.ask(reset)
		return self.ask("INPut:PDIode:FILTer:STATe?")

							#   --------------------------------------------------------  #
	# Setting the Thermopile Accelerator State ON and OFF (ON/OFF/1/0)
	def set_thermo_accel(self,mode):
		self.ask(reset)
		self.ask("*OPC?;" + "INPut:THERmopile:ACCelerator:STATe " + mode)

	# Getting the Thermopile Accelerator State (Enable/Disable) (ON/OFF/1/0)
	def get_thermo_accel(self):
		self.ask(reset)
		return self.ask("INPut:THERmopile:ACCelerator:STATe?")

	# Setting the Thermopile Accelerator AUTO Mode ON and OFF (ON/OFF/1/0)
	def set_thermo_accel_auto(self,mode):
		self.ask(reset)
		self.ask("*OPC?;" + "INPut:THERmopile:ACCelerator:AUTO " + mode)

	# Getting the Thermopile Accelerator AUTO Mode (Enable/Disable) (ON/OFF/1/0)
	def get_thermo_accel_auto(self):
		self.ask(reset)
		return self.ask("INPut:THERmopile:ACCelerator:AUTO?")

	# Setting the Thermopile Time Constant [0 - 63]% in [s] 
	def set_thermo_time_const(self,mode):
		self.ask(reset)
		self.ask("*OPC?;" + "INPut:THERmopile:ACCelerator:TAU " + mode)

	# Getting the Thermopile Time Constant in [s] 
	def get_thermo__time_const(self):
		self.ask(reset)
		return self.ask("INPut:THERmopile:ACCelerator:TAU?")

							#   --------------------------------------------------------  #
	# Setting the Default Sensor Adapter type (PHOT/THER/PYR)
	def set_sensor_adapter(self,sensor):
		self.ask(reset)
		self.ask("*OPC?;" + "INPut:ADAPter:TYPE " + sensor)

	# Getting the Thermopile Accelerator State (Enable/Disable) (ON/OFF/1/0)
	def get_sensor_adapter(self):
		self.ask(reset)
		return self.ask("INPut:ADAPter:TYPE?")


							#   --------------------------------------------------------  #
	# Setting a Measurement Configuration POW/CURR/VOLT/ENER/FREQ/PDEN/EDEN/RES/TEMP
	def set_meas_config(self,config):
		self.ask(reset)
		self.ask("CONF?;CONFigure:" + config)

	# Perform a Measurement POW/CURR/VOLT/ENER/FREQ/PDEN/EDEN/RES/TEMP
	def get_meas(self,meas):
		self.set_meas_config(meas)
		self.ask(reset)
		return self.ask("READ?;MEAS:" + meas)

