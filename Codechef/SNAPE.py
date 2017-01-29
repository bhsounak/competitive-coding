for _ in range(int(raw_input())):
	B, LS=map(int, raw_input().split())
	print (LS**2-B**2)**0.5, (B**2+LS**2)**0.5
