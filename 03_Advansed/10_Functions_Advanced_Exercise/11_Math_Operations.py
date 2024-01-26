def math_operations(*numbers, **kwargs):
    keys = list(kwargs.keys())
    for idx in range(len(numbers)):
        key = keys[idx % 4]
        if key == "a":
            kwargs[key] += numbers[idx]
        elif key == "s":
            kwargs[key] -= numbers[idx]
        elif key == "d":
            if numbers[idx] != 0:
                kwargs[key] /= numbers[idx]
        elif key == "m":
            kwargs[key] *= numbers[idx]
    result = []
    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result.append(f"{key}: {value:.1f}")
    return '\n'.join(result)


print(math_operations(6.0, a=0, s=0, d=5, m=0))
