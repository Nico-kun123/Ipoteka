class MortgageCalculator:
    def __init__(self, principal, annual_rate, years, fixed_rate=True, additional_payments=0):
        
        try:
            annual_rate = float(annual_rate)
        except ValueError:
            raise TypeError("Annual_rate must be a numeric value.")

        if not all(isinstance(arg, (int, float)) for arg in (principal, annual_rate, years, additional_payments)):
            raise TypeError("Principal, annual_rate, years, and additional_payments must be numeric values.")
        
        if not isinstance(fixed_rate, bool):
            raise TypeError("Fixed_rate must be a boolean value.")

        if principal <= 0 or annual_rate <= 0 or years <= 0:
            raise ValueError("Principal, annual_rate, and years must be positive values.")
        
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
        self.fixed_rate = fixed_rate
        self.additional_payments = additional_payments

    def calculate_monthly_payment(self):
        monthly_rate = self.annual_rate / 12 / 100
        num_payments = self.years * 12

        if self.fixed_rate:
            monthly_payment = (
                self.principal
                * monthly_rate
                * (1 + monthly_rate) ** num_payments
            ) / ((1 + monthly_rate) ** num_payments - 1)
        else:
            monthly_payment = (
                self.principal
                * monthly_rate
                * (1 + monthly_rate) ** num_payments
            ) / ((1 + monthly_rate) ** num_payments - 1)

        monthly_payment += self.additional_payments

        return round(monthly_payment, 2)


def main():
    principal = float(input("\nВведите сумму ипотеки: "))
    annual_rate = float(input("Введите количество годовых процентов (%): "))
    years = int(input("Введите количество лет: "))

    fixed_rate = input("Фиксированная или переменная ставка? (Введите 'fixed' или 'var'): ").lower() == "fixed"
    additional_payments = float(input("Введите дополнительные ежемесячные выплаты (если таковые есть): "))

    calculator = MortgageCalculator(principal, annual_rate, years, fixed_rate, additional_payments)
    monthly_payment = calculator.calculate_monthly_payment()

    print(f"\nВаша ежемесячная выплата: ${monthly_payment} ({calculator.fixed_rate, calculator.additional_payments})\n")


if __name__ == "__main__":
    main()
