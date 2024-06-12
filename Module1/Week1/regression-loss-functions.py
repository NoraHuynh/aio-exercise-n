import random
import math


def calculate_uni_loss(y_target, y_pred, loss_name):
    if loss_name == "MAE":
        loss = math.fabs(y_target - y_pred)
    else:
        loss = (y_target - y_pred) ** 2
    return loss


class LossFunction:

    def calculate_mae(self, n, sum_loss):
        mae = (1 / n) * sum_loss
        return mae

    def calculate_mse(self, n, sum_loss):
        mse = (1 / n) * sum_loss
        return mse

    def calculate_rmse(self, n, sum_loss):
        mse = (1 / n) * sum_loss
        rmse = math.sqrt(mse)
        return rmse

    def calculate_loss_function(self, n, sum_loss, loss_name):
        if loss_name.upper() == "MAE":
            result = self.calculate_mae(n, sum_loss)
            return result
        elif loss_name.upper() == "MSE":
            result = self.calculate_mse(n, sum_loss)
            return result
        else:
            result = self.calculate_rmse(n, sum_loss)
            return result


def exercise3():
    num_samples = input(
        "Input number of samples (integer number) which are generated: "
    )
    if num_samples.isnumeric() == False:
        print("number of samples must be an integer number")
    else:
        n = int(num_samples)
        loss_name = input("loss name: ")
        loss_name_lst = ["MAE", "MSE", "RMSE"]
        if loss_name.upper() not in loss_name_lst:
            print(f"{loss_name} is not supported")
        else:
            loss_f = LossFunction()
            loss_name = loss_name.upper()
            sum_loss = 0
            for idx in range(n):
                y_target = random.uniform(0, 10)
                y_pred = random.uniform(0, 10)
                loss = calculate_uni_loss(y_target, y_pred, loss_name=loss_name)
                print(
                    f"loss name: {loss_name}, sample: {idx}, pred: {y_pred}, target: {y_target}, loss: {loss}"
                )
                sum_loss += loss
            result = loss_f.calculate_loss_function(n, sum_loss, loss_name)
            print(f"final {loss_name}: {result}")


exercise3()
