document.getElementById('registrationForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // 简单的验证
    if (username.length < 3) {
        document.getElementById('message').textContent = '用户名至少需要 3 个字符。';
        return;
    }

    if (password.length < 6) {
        document.getElementById('message').textContent = '密码至少需要 6 个字符。';
        return;
    }

    // 模拟注册成功
    document.getElementById('message').textContent = '注册成功！';
    document.getElementById('registrationForm').reset();
});
