# 团队排序算法整合项目 - 初始框架
# 项目名称：First_Main_202441903104
# 开发规范：遵循驼峰命名、注释完整、格式统一
# 排序算法函数预留区域：组内成员依次在下方添加自己的算法
# 示例格式：def 姓名首拼_算法名(参数): 如 zsBubbleSort(arr)


# 快速排序
# 功能: 对数字数组进行升序排序
# 参数: arr - 待排序的数字数组
# 返回值: sortedArr - 排序后的升序数组
def szyQuickSort(arr):
    # 复制原数组，避免修改原数据
    sortedArr = arr.copy()

    def quickSortCore(subArr):
        # 递归终止条件：数组长度小于等于1直接返回
        if len(subArr) <= 1:
            return subArr
        # 选取基准元素
        pivot = subArr[len(subArr) // 2]
        # 小于基准的元素
        left = [x for x in subArr if x < pivot]
        # 等于基准的元素
        middle = [x for x in subArr if x == pivot]
        # 大于基准的元素
        right = [x for x in subArr if x > pivot]
        # 递归左右子数组，合并结果
        return quickSortCore(left) + middle + quickSortCore(right)

    return quickSortCore(sortedArr)

# 程序运行测试入口：所有成员最终在此处调用自己的算法
if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]
    print("原始测试数组：", testArr)
    # 成员调用自己的算法：后续在此处添加代码
