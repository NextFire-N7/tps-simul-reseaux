import asyncio

import numpy as np
import matplotlib.pyplot as plt
from itertools import chain


async def test(idle: float):
    outfile = f'/tmp/res{idle}.tr'
    proc = await asyncio.create_subprocess_shell("ns ../sat-aloha.tcl poisson",
                                                 shell=True,
                                                 env={
                                                     'IDLE': str(idle),
                                                     'OUTFILE': outfile
                                                 })
    await proc.communicate()
    proc = await asyncio.create_subprocess_shell(f"perl loss.pl {outfile}",
                                                 shell=True,
                                                 stdout=asyncio.subprocess.PIPE)
    stdout, _ = await proc.communicate()
    rho_0, rho_s = stdout.decode().splitlines()[-1].split()[-2:]
    print(idle, rho_0, rho_s)
    return float(rho_0), float(rho_s)


async def main():
    res = await asyncio.gather(
        *(test(i)
          for i in chain(np.arange(0.01, 0.3, 0.01), np.arange(0.3, 5, 0.1))))
    with open('res.txt', 'w') as f:
        for rho_0, rho_s in res:
            print(rho_0, rho_s, file=f)
    rho_0s, rho_ss = zip(*res)
    plt.scatter(rho_0s, rho_ss)
    plt.grid()
    plt.xlabel(r'$\rho_0$')
    plt.ylabel(r'$\rho_s$')
    plt.xlim(right=1)
    plt.show()


asyncio.run(main())
