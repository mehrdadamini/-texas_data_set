def displalymulty(wells,logname):
    fig, ax = plt.subplots(figsize=(8, 6))
    for label, data in wells:
      data.logname.plot(kind = 'kde', ax = ax, label = label)
      plt.xlim(data.logname.min(),data.logname.max())
    plt.grid(True)
    plt.legend()
    return plt.show()