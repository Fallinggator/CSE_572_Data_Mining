def main():  
  # Read CGMData.csv
  cgm_data = pd.read_csv('CGMData.csv', usecols=['Date','Time', 'Sensor Glucose (mg/dL)'], parse_dates=[['Date', 'Time']])

  # Read InsulinData.csv
  insulin_data = pd.read_csv('InsulinData.csv', usecols=['Date','Time', 'Alarm'], parse_dates=[['Date', 'Time']])

  # Find timestamp for Auto Mode from InsulinData.csv
  auto_mode_ts = insulin_data[insulin_data['Alarm'] == 'AUTO MODE ACTIVE PLGM OFF']['Date_Time'].min()

  # Find timestamp for start of Auto Mode in CGMData.csv
  cgm_auto_ts = cgm_data[cgm_data['Date_Time'] >= auto_mode_ts]['Date_Time'].min()