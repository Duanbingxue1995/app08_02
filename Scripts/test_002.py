import allure
class Test_001:
    @allure.step(title="测试1")
    def test_01(self):
        print("--test_01")
        assert True
    @allure.step(title="测试2")
    def test_02(self):
        print("--test_02")
        assert False
