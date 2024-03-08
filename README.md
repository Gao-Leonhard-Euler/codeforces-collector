# Codeforces 内容收集器/Codeforces Collector

## Codeforces 提交记录收集器/Codeforces Submission Collector

`CodeforcesCollect_Submission.py`

这个Python脚本可以帮助用户从Codeforces平台收集和保存提交记录并对其进行分类。

This Python script can help users collect and save submission records from the Codeforces platform and categorize them.

### 使用方法/Usage

1. **安装依赖**：确保你的Python环境中安装了`requests`和`html`库。如果没有安装，可以通过以下命令安装：

   **Dependencies Installation**: Ensure that the `requests` and `html` libraries are installed in your Python environment. If not installed, you can install them using the following commands:
   
   ```
   pip install requests
   pip install html
   ```

3. **运行脚本**：在命令行中运行脚本，脚本会提示你输入想要查找的样例个数(不大于1000)。输入一个整数`t`，脚本将获取最近的`t`个提交记录，将其中有权限访问的记录保存并分类。

   **Running the Script**: Execute the script in the command line, where the script will prompt you to enter the number of samples you wish to search for (not exceeding 1000). Enter an integer `t`, and the script will proceed to retrieve the specified number of submissions.

4. **查看结果**：脚本会在当前工作目录下创建相应的文件夹结构，并保存提交记录。文件夹结构为`比赛编号/问题编号/编程语言/评测结果`，提交记录保存的文件格式为`提交编号.txt`，评测结果分为`goodCase`（通过）和`badCase`（失败）。

   **Reviewing the Results**: The script will create the corresponding folder structure in the current working directory and save the submission records. The folder structure will be in the format of `Contest ID/Problem Index/Programming Language/Verdict Result`. The submission records will be saved in files named with the submission ID followed by `.txt`. The verdict results are categorized as `goodCase` (accepted) and `badCase` (failed).

### 注意事项/Note

- 请确保你的网络连接正常，以便脚本能够成功访问Codeforces的API。
- Ensure that your internet connection is stable so that the script can successfully access the Codeforces API.
- 脚本在运行过程中可能会遇到连接失败或网络延迟，如果请求失败，它会自动重试。
- The script may encounter connection failures or network delays during execution. If a request fails, it will automatically retry.
- 请确保你的Python环境版本与脚本兼容。
- Make sure that your Python environment version is compatible with the script.

## LICENSE

本项目采用**CC BY-NC-SA 4.0**知识共享许可协议。如需了解该协议，请查阅[https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans)\
This work is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit [https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)
