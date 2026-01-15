# 🤖 Local AI Chatbot with Ollama

Dự án chatbot đơn giản giúp bạn trò chuyện với các mô hình ngôn ngữ lớn (LLM) ngay trên máy tính cá nhân, hoàn toàn miễn phí và không cần internet.

## ✨ Tính năng
- Sử dụng thư viện `openai` để giao tiếp với **Ollama**.
- Hỗ trợ phản hồi dạng stream (chữ hiện ra đến đâu xem đến đó).
- Lưu lại lịch sử hội thoại trong phiên làm việc.

## 🛠 Yêu cầu hệ thống
1. **Ollama:** Đã cài đặt và đang chạy tại `localhost:11434`.
2. **Model:** Đã tải model (Ví dụ: `gemma3:1b`).
3. **Python:** Phiên bản 3.x.

## 🚀 Hướng dẫn cài đặt

### Bước 1: Cài đặt thư viện
```bash
pip install openai
```

### Bước 2: Tải mô hình AI
Mở Terminal và chạy lệnh:
```bash
ollama pull gemma3:1b
```

### Bước 3: Chạy ứng dụng
```bash
python AI_bot.py
```

## 📖 Cách sử dụng
- Gõ nội dung bạn muốn hỏi và nhấn Enter.
- Gõ exit để thoát chương trình.
