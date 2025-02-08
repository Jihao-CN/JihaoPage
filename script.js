let selectedMenuItem = -1;
const audio = document.getElementById('bgm');
const audioControl = document.getElementById('audio-control');

audio.volume = 0.2; // 设置默认音量

audio.addEventListener('ended', () => {
    audioControl.classList.add('paused');
});

function selectMenuItem(index) {
    // 移除之前选中的菜单项的样式
    if (selectedMenuItem !== -1) {
        document.querySelectorAll('.menu-item')[selectedMenuItem].classList.remove('selected');
        document.querySelectorAll('.content-item')[selectedMenuItem].classList.remove('active');
    }

    // 更新选中的菜单项索引
    selectedMenuItem = index;

    // 添加当前选中的菜单项的样式
    document.querySelectorAll('.menu-item')[index].classList.add('selected');
    document.querySelectorAll('.content-item')[index].classList.add('active');
}

function togglePlayPause() {
    if (audio.paused) {
        audio.play();
        audioControl.classList.remove('paused');
    } else {
        audio.pause();
        audioControl.classList.add('paused');
    }
}