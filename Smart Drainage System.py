flow_volume = 0
flow_rate = 0
flow_count = 0
flow_pin = pins.digital_read_pin(DigitalPin.P0)
# Set up timer for one second
timer = input.running_time()

def on_every_interval():
    global flow_pin, flow_count, flow_rate, flow_volume
    flow_pin = pins.digital_read_pin(DigitalPin.P0)
    # Read the flow sensor input
    if flow_pin == 1:
        flow_count += 1
        basic.show_icon(IconNames.YES)
    elif flow_pin == 0:
        basic.show_icon(IconNames.NO)
        # Calculate the flow rate and volume
        flow_rate = flow_count * 0.1
        # litter per second(assuming 1 count = 0.1 L/s)
        flow_volume = flow_rate * timer
        # log the data
        datalogger.log(datalogger.create_cv("flow count", flow_count),
            datalogger.create_cv("flow _volume  (L)", flow_volume),
            datalogger.create_cv("flow __ rate (l/second", flow_rate))
        if flow_rate <= 0:
            music.start_melody(music.built_in_melody(Melodies.DADADADUM),
                MelodyOptions.ONCE)
            basic.show_string("choking")
loops.every_interval(500, on_every_interval)
