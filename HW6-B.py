account = input()
normalized = "_".join(account.strip(" ").lower().split())

is_valid = 6 <= len(normalized) <= 16 and all(
	"a" <= char <= "z" or "0" <= char <= "9" or char == "_"
	for char in normalized
)

print(normalized)
print("VALID" if is_valid else "INVALID")
