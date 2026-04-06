from django.shortcuts import render, redirect


def home(request):
    return render(request, "home.html", {"name": "Abed Khan"})


def calculate(request):
    if request.method != "POST":
        return redirect("home")

    operation = request.POST.get("operation", "+")
    try:
        val1 = float(request.POST["num1"])
        val2 = float(request.POST["num2"])
    except (KeyError, ValueError):
        return render(
            request,
            "result.html",
            {"error": "Please enter valid numbers for both fields."},
        )

    if operation == "+":
        result = val1 + val2
    elif operation == "-":
        result = val1 - val2
    elif operation == "*":
        result = val1 * val2
    elif operation == "/":
        if val2 == 0:
            return render(
                request,
                "result.html",
                {"error": "Cannot divide by zero."},
            )
        result = val1 / val2
    else:
        return render(
            request,
            "result.html",
            {"error": "Invalid operation selected."},
        )

    op_labels = {"+": "+", "-": "−", "*": "×", "/": "÷"}
    
    return render(
        request,
        "result.html",
        {
            "result": result,
            "val1": val1,
            "val2": val2,
            "operation": operation,
            "operation_label": op_labels.get(operation, operation),
        },
    )
