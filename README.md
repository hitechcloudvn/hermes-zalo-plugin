<div align="center">

# hermes-zalo-plugin

**Plugin Hermes kết nối tài khoản Zalo cá nhân qua sidecar Node.js (`zca-js`)**

**Hermes plugin connecting a personal Zalo account via a Node.js sidecar (`zca-js`)**

[![CI](https://github.com/hitechcloudvn/hermes-zalo-plugin/actions/workflows/ci.yml/badge.svg)](https://github.com/hitechcloudvn/hermes-zalo-plugin/actions/workflows/ci.yml)
[![Release](https://github.com/hitechcloudvn/hermes-zalo-plugin/actions/workflows/release.yml/badge.svg)](https://github.com/hitechcloudvn/hermes-zalo-plugin/actions/workflows/release.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Made in Vietnam](https://img.shields.io/badge/Made%20in-Vietnam-DA251D?style=flat-square)](https://hitechcloud.vn)

**Tiếng Việt** | **English**

[GitHub](https://github.com/hitechcloudvn/hermes-zalo-plugin) · [GitLab](https://gitlab.com/hitechcloudvn/hermes-zalo-plugin)

</div>

---

## 🇻🇳 Tiếng Việt

### Giới thiệu

`hermes-zalo-plugin` là [plugin cho Hermes Agent](https://hermes-agent.nousresearch.com) kết nối **tài khoản Zalo cá nhân** thông qua một **sidecar Node.js** dùng thư viện `zca-js` (Zalo Web API không chính thức). Bot nhận/gửi tin nhắn Zalo, trả lời như một trợ lý AI cá nhân, hỗ trợ marketing, nhắc hẹn và gửi file ngay trong chat.

> ⚠️ **CẢNH BÁO QUAN TRỌNG**
>
> * Đây là API Zalo **không chính thức**.
> * **Khuyến nghị sử dụng tài khoản phụ**, không dùng tài khoản Zalo chính.
> * Gửi lời mời kết bạn hoặc tin nhắn hàng loạt có thể khiến tài khoản bị hạn chế hoặc khóa.
> * Người dùng tự chịu trách nhiệm khi sử dụng phần mềm này.
> * Luôn tuân thủ Điều khoản sử dụng của Zalo và các quy định pháp luật liên quan.

### Tính năng

* Nhận và gửi tin nhắn Zalo cá nhân và nhóm; ảnh, file, sticker, reaction, trạng thái "đang nhập".
* Chế độ chat linh hoạt: `active` / `mention_only` / `listen_only` / `mute` — đổi bằng lệnh `/bot` hoặc nói tự nhiên.
* Persona riêng cho từng nhóm (nhiệm vụ + phong cách), persona chung cho câu hỏi "em là ai".
* Cảnh báo từ khoá trong nhóm, daily digest 8h sáng về DM của chủ.
* Nhắc hẹn động (Osin-style): nhiều mốc giờ, nấc thang nhắc lại, soạn tin bằng LLM toolless + template dự phòng.
* Phễu marketing: quét thành viên nhóm từ link `zalo.me/g/...`, tra SĐT → UID, kết bạn, nhắn tin AI cá nhân hoá, đồng bộ Google Sheet CRM.
* Tạo và gửi file HTML, PDF, PowerPoint, Excel; gửi ảnh có tự động downscale.
* Chào nhóm tự động khi bot được thêm vào; tự động chấp nhận lời mời kết bạn (trong hạn mức ngày).
* Tự nhắn lại khi có cuộc gọi nhỡ; mode bảo trì (`/bot baotri`) thông báo khách tự động.
* eKYC link cũ (`tino.vn/ekyc/...`, `*.hitechcloud.vn/api/vneidekyc/ekyc/...`) tự chuyển sang Zalo mini-app.

### Cài đặt

1. Clone plugin vào thư mục plugin của Hermes:
   ```bash
   git clone https://github.com/hitechcloudvn/hermes-zalo-plugin.git ~/.hermes/plugins/hermes-zalo-plugin
   ```
2. Cài dependencies cho sidecar:
   ```bash
   cd ~/.hermes/plugins/hermes-zalo-plugin/sidecar
   npm ci || npm install
   ```
3. (Tùy chọn) Cài thêm package Python: `google-api-python-client`, `google-auth` (Google Sheet); `Pillow` (downscale ảnh).
4. Copy `.env.example` thành `.env` (hoặc khai báo trong cấu hình Hermes) rồi điền biến môi trường.
5. Khởi động lại Hermes. Lần đầu đăng nhập Zalo bằng QR Code (session lưu tại `ZALO_PERSONAL_SESSION_DIR`).
6. Thiết lập `ZALO_PERSONAL_OWNER_UID` — chỉ UID này được toàn quyền điều khiển bot.

### Cấu hình

Biến môi trường (xem thêm `.env.example`):

| Biến | Bắt buộc | Mặc định | Mô tả |
|---|---|---|---|
| `ZALO_PERSONAL_OWNER_UID` | ✅ | — | Zalo UID của chủ tài khoản (người điều khiển bot). Chỉ user này được toàn quyền. |
| `ZALO_PERSONAL_OWNER_USER_ID` | | = `OWNER_UID` | Hermes user_id để map identity/memory. |
| `ZALO_PERSONAL_ALLOWED_USERS` | | — | Danh sách Zalo UID khác (phẩy ngăn cách) cũng được phép chat. |
| `ZALO_PERSONAL_SIDECAR_PORT` | | `3838` | Port sidecar Node.js (127.0.0.1). |
| `ZALO_PERSONAL_PROXY` | | — | Proxy cho sidecar (`http://user:pass@host:port` hoặc `socks5://...`). Khuyến nghị proxy dân cư cùng quốc gia với số Zalo. |
| `ZALO_PERSONAL_SESSION_DIR` | | `/opt/data/zalo` | Thư mục lưu session + dữ liệu. PHẢI giống nhau cho cả sidecar Node và adapter Python. |
| `ZALO_PERSONAL_MAX_CONCURRENT_DOWNLOADS` | | `4` | Số lượt tải media đồng thời tối đa của sidecar. |
| `HITECHCLOUD_LANDING_BRIDGE_URL` | | `https://mcp.hitechcloud.vn/tools/landing_upload_image` | Endpoint upload ảnh Zalo → landing (server-to-server). |
| `HITECHCLOUD_LANDING_BRIDGE_KEY` | | — | Key riêng chỉ được gọi `landing_upload_image`. Chỉ đọc từ env, không log, không đưa qua model. |
| `ZALO_PERSONAL_GROUP_GREETING` | | `true` | Tự chào cả nhóm khi bot được thêm vào (mỗi group 1 lần). |
| `ZALO_PERSONAL_AUTO_FRIEND_ON_DM` | | `true` | Người lạ DM → tự gửi lời mời kết bạn (dùng chung hạn mức `daily_friend_cap`). |
| `ZALO_PERSONAL_AUTO_FRIEND_MSG` | | `Mình kết bạn để tiện hỗ trợ nhé!` | Lời nhắn kèm lời mời kết bạn tự động. |
| `ZALO_PERSONAL_NAME_TRIGGERS` | | — | Tên gọi kích hoạt bot trong nhóm (phẩy ngăn cách, vd `ông bụt,bụt`) — không cần @tag. |
| `ZALO_OWNER_NICKNAME` | | `sếp` | Cách bot xưng hô với chủ. |
| `ZALO_OWNER_NAME` | | — | Tên thật của chủ cần CHE nếu bot lỡ nhắc. Bỏ trống = không che. |
| `GOOGLE_TOKEN_PATH` | | — | Đường dẫn `google_token.json` (OAuth Google) để bật xuất Google Sheet. |
| `ZALO_PERSONAL_HOME_THREAD` | | — | Thread/chat ID mặc định để cron/notification đẩy về. |
| `ZALO_IMAGE_URL_ALLOWED_HOSTS` | | `mcp.hitechcloud.vn` | Host cho phép khi `zalo_send_image` tải ảnh từ `image_url` (phẩy ngăn cách). Chống SSRF. Nếu set, PHẢI tự kèm `mcp.hitechcloud.vn` nếu vẫn cần gửi QR. |

### Công cụ (Tools)

Bot đăng ký 52 công cụ cho agent. Chú ý: công cụ marketing/quét/kết bạn chỉ dùng cho mục đích hợp pháp, có hạn mức ngày để tránh khoá tài khoản.

| Công cụ | Mô tả |
|---|---|
| `zalo_groups_list` | Liệt kê nhóm bot đã tham gia (group_id, số thành viên, hoạt động gần nhất, shared_session_id). |
| `zalo_set_chat_mode` | Owner-only: đổi mode hành vi của bot cho một chat. |
| `zalo_get_chat_mode` | Xem mode + cài đặt hiện tại của một chat. |
| `zalo_set_digest` | Owner-only: bật/tắt daily digest (tổng hợp 8h sáng) cho một chat. |
| `zalo_set_persona` | Owner-only: cập nhật persona (tên, giới thiệu, tính cách) của bot. |
| `zalo_get_persona` | Xem persona hiện tại của bot. |
| `zalo_reset_persona` | Owner-only: khôi phục persona mặc định. |
| `zalo_set_chat_persona` | Owner-only: set nhiệm vụ + phong cách riêng cho từng group/chat. |
| `zalo_get_chat_persona` | Owner-only: xem persona riêng + persona hiệu lực của một chat. |
| `zalo_group_summary` | Lấy tin nhắn gần đây của nhóm (qua shared session) để tóm tắt / hỏi đáp. |
| `zalo_react` | Thả reaction vào tin nhắn gần nhất trong chat hiện tại. |
| `zalo_send_sticker` | Gửi sticker hợp ngữ cảnh (keyword = từ khoá cảm xúc). |
| `zalo_set_reactions` | Owner-only: bật/tắt thả reaction ở một chat. |
| `zalo_add_keyword_alert` | Owner-only: đăng ký cảnh báo theo từ khoá trong nhóm. |
| `zalo_list_keyword_alerts` | Liệt kê các luật cảnh báo từ khoá. |
| `zalo_remove_keyword_alert` | Owner-only: xoá một luật cảnh báo từ khoá. |
| `zalo_toggle_keyword_alert` | Owner-only: bật/tắt luật cảnh báo mà không xoá. |
| `zalo_list_products` | Liệt kê catalog sản phẩm cho sales mode (owner-only). |
| `zalo_add_product` | Thêm/cập nhật 1 sản phẩm vào catalog (owner-only). |
| `zalo_update_product` | Cập nhật từng phần 1 sản phẩm (owner-only). |
| `zalo_remove_product` | Xoá 1 sản phẩm khỏi catalog (owner-only). |
| `zalo_update_sales_rules` | Cập nhật quy tắc an toàn sales mode (cooldown, quota, avoid keyword). |
| `zalo_record_sales_pitch` | Ghi nhận vừa gửi 1 pitch để cập nhật cooldown + quota ngày. |
| `zalo_sales_quota` | Xem trạng thái sales quota của một nhóm (còn pitch được không, vì sao). |
| `zalo_send_html` | Owner-only: tạo file HTML từ nội dung và gửi vào chat Zalo. |
| `zalo_send_pdf` | Render HTML → PDF (WeasyPrint) rồi gửi vào chat (báo giá, hợp đồng, brochure). |
| `zalo_send_file` | Gửi thẳng file có sẵn (docx, zip, mp3…) từ URL công khai vào chat. |
| `zalo_send_pptx` | Tạo PowerPoint từ spec slides rồi gửi vào chat Zalo. |
| `zalo_send_xlsx` | Tạo Excel từ spec sheets/rows rồi gửi vào chat Zalo. |
| `zalo_send_image` | Gửi ảnh cho khách — ưu tiên `image_url` nội bộ, adapter tự tải (không phình context). |
| `zalo_escalate_to_owner` | Báo sếp qua DM Zalo khi bí / khách cần người thật (có cooldown chống spam). |
| `zalo_friend_add` | Kết bạn với một người (gửi lời mời kết bạn). |
| `zalo_friend_accept` | Chấp nhận lời mời kết bạn từ một uid. |
| `zalo_friend_sync` | Đối chiếu danh bạ — đánh dấu lead đã chấp nhận kết bạn. |
| `zalo_send_dm` | Nhắn tin trực tiếp cho một người, kèm nhiều ảnh nếu cần. |
| `zalo_scan_group` | Quét thành viên nhóm theo link `zalo.me/g/...` (không cần tham gia; quét nền dàn trải ~24h). |
| `zalo_master_sheet` | Lấy link Google Sheet chung quản lý lead + đồng bộ trạng thái mới nhất. |
| `zalo_lookup_phones` | Tra danh sách SĐT → tài khoản Zalo (uid, tên) → tạo lead + Sheet. |
| `zalo_marketing_prepare` | Chuẩn bị đợt kết bạn/nhắn tin theo hạn mức ngày — trả lead + brief cho agent soạn nội dung. |
| `zalo_marketing_send` | Gửi đợt marketing đã soạn SAU KHI sếp duyệt (kèm ảnh tuỳ chọn). |
| `zalo_marketing_settings` | Xem/đổi hạn mức marketing, bật/tắt tự động chấp nhận kết bạn. |
| `zalo_campaign_report` | Báo cáo phễu marketing (đã quét → mời → đồng ý → đã nhắn). |
| `zalo_campaign_sync` | Đồng bộ Google Sheet của chiến dịch từ kho lead. |
| `zalo_create_poll` | Tạo poll (bình chọn) trong nhóm Zalo hiện tại. |
| `zalo_create_note` | Tạo ghi chú lên bảng tin nhóm Zalo (có thể ghim). |
| `zalo_create_reminder` | Tạo nhắc hẹn NATIVE trên Zalo — chỉ khi sếp nói rõ chữ "zalo". |
| `zalo_schedule_reminder` | Đặt lịch nhắc trong nhóm: tới giờ bot tự gửi tin nhắc, tag @người. |
| `zalo_board_action` | Thao tác bảng tin nhóm: list note/poll/reminder, poll_vote, poll_lock, note_edit… |
| `zalo_read_recent_image` | Lấy ảnh gần nhất khách gửi trong chat hiện tại (giữ 5 ảnh/chat). |
| `zalo_upload_recent_image_to_landing` | Đưa ảnh gần nhất khách gửi lên landing demo của hội thoại, trả `image_url` công khai. |
| `set_channel_active` | Owner-only: bật/tắt một kênh bot (vd `telegram-personal`). |
| `zalo_api_call` | Owner-only — power tool: gọi trực tiếp bất kỳ method zca-js nào. |

### Lệnh owner (`/bot`)

Chỉ chủ tài khoản (owner) dùng — nhắn trong DM hoặc trong nhóm mà bot tham gia:

| Lệnh | Tác dụng |
|---|---|
| `/bot status` | Xem trạng thái chat hiện tại (mode, daily_digest, chat_id). |
| `/bot mode <type>` | Đổi mode: `active` / `mention_only` / `listen_only` / `mute` / `default`. |
| `/bot modes` | Liệt kê các mode và ý nghĩa. |
| `/bot digest <on\|off>` | Bật/tắt daily digest cho chat này. |
| `/bot baotri` | Xem trạng thái mode bảo trì. |
| `/bot baotri <câu+giờ>` | BẬT bảo trì với câu thông báo tự gửi khách (vd `Bọn em bảo trì tới 15h30 hôm nay ạ`). |
| `/bot baotri on\|off` | Bật (câu mặc định) / tắt mode bảo trì. |
| `/bot help` | Hiện trợ giúp. |

Các mode chat:

| Mode | Hành vi |
|---|---|
| `active` | Bot phản hồi mọi tin trong chat (không cần tag). |
| `mention_only` | Chỉ phản hồi khi @mention hoặc reply tin của bot (mặc định). |
| `listen_only` | Đọc + lưu context, KHÔNG phản hồi. |
| `mute` | Bỏ qua hoàn toàn chat này. |
| `default` | Theo cấu hình global (`mention_only`). |

Ngoài ra owner có thể nói tự nhiên ("em theo dõi group này tích cực", "đừng phản hồi gì ở đây nữa") — bot tự đổi mode tương ứng.

### Nhắc hẹn (reminders)

* **Nhắc hẹn nhóm** (`zalo_schedule_reminder`): đặt nhiều mốc giờ (`fire_times`), tới giờ bot tự gửi tin nhắn nhắc và tag `@người`. Càng về sau mức nhắc càng mạnh (nấc thang theo lần nhắc).
* **Nhắc hẹn native** (`zalo_create_reminder`): tạo reminder trên bảng tin Zalo — chỉ dùng khi sếp nói rõ chữ "zalo".
* **Soạn tin nhắc** (`reminder_compose.py`): LLM toolless (không agent, không tool) soạn câu nhắc tiếng Việt; lỗi/rỗng → template dự phòng. Toàn bộ nội dung nhắc được xử lý như DỮ LIỆU người dùng (chống injection), `@All` / tag tên chủ bị gỡ ký hiệu `@` trước khi gửi.

### Pipeline media

* **Media đến**: sidecar tải streaming theo hợp đồng `media-contract.js` (giới hạn dung lượng, sniff magic bytes, không tin phần mở rộng file); cache tại `<session_dir>/media-cache/` với tên theo nội dung (`<stem>-<sha256[:12]>.<ext>`).
* **Gửi ảnh** (`zalo_send_image` + `image_url_fetch.py` + `image_resize.py`): chỉ tải ảnh từ host trong `ZALO_IMAGE_URL_ALLOWED_HOSTS` (chống SSRF), xác thực magic bytes, tự downscale cạnh dài về 1024 (mặc định) nếu có Pillow.
* **Bridge landing** (`landing_media_bridge.py`): ảnh khách gửi trong chat được đưa lên landing demo **server-to-server** qua `HITECHCLOUD_LANDING_BRIDGE_URL` + key riêng — KHÔNG chuyển base64 qua LLM. Đọc cache fail-closed: chặn path escape, symlink, file không phải ảnh, file quá lớn.
* **eKYC rewrite**: link eKYC cũ trong tin nhắn ra tự chuyển sang Zalo mini-app (token giữ nguyên ở path).

### Kiểm thử

```bash
# Python (pytest)
python -m pytest -q

# Sidecar Node.js (node:test)
cd sidecar && npm ci || npm install && node --test
```

### Giấy phép & Miễn trừ trách nhiệm

MIT — xem [LICENSE](LICENSE). © 2026 HiTechCloud.VN.

Phần mềm được cung cấp theo nguyên trạng ("AS IS"), không có bất kỳ cam kết hay bảo hành nào. Việc sử dụng API Zalo không chính thức có thể dẫn đến việc tài khoản bị hạn chế hoặc khóa. Người dùng tự chịu trách nhiệm; luôn tuân thủ Điều khoản sử dụng của Zalo và pháp luật hiện hành.

---

## 🇬🇧 English

### Overview

`hermes-zalo-plugin` is a [Hermes Agent](https://hermes-agent.nousresearch.com) plugin that connects a **personal Zalo account** through a **Node.js sidecar** using the `zca-js` library (an unofficial Zalo Web API). The bot sends and receives Zalo messages, replies as a personal AI assistant, and supports marketing funnels, reminders, and file delivery right inside the chat.

> ⚠️ **IMPORTANT DISCLAIMER**
>
> * This project uses an **unofficial Zalo API**.
> * It is strongly recommended to use a **secondary Zalo account**, not your primary account.
> * Excessive friend requests or bulk messaging may result in account restrictions or bans.
> * Users are solely responsible for how they use this software.
> * Always comply with Zalo's Terms of Service and applicable privacy regulations.

### Features

* Send and receive Zalo direct and group messages; images, files, stickers, reactions, typing indicators.
* Flexible chat modes: `active` / `mention_only` / `listen_only` / `mute` — switch via `/bot` commands or plain language.
* Per-group persona (mission + style) plus a global persona for "who are you?" questions.
* Keyword alerts in groups; daily digest delivered to the owner's DM at 8 AM (VN).
* Dynamic (Osin-style) reminders: multiple fire times, escalating retries, toolless-LLM composition with template fallback.
* Marketing funnel: group-member scan from `zalo.me/g/...` links, phone → UID lookup, friend requests, AI-personalized outreach, Google Sheet CRM sync.
* Generate and send HTML, PDF, PowerPoint, and Excel files; images are auto-downscaled on send.
* Auto-greet on group join; auto-accept friend requests (within the daily cap).
* Missed-call auto-reply; maintenance mode (`/bot baotri`) that auto-notifies customers.
* Legacy eKYC links (`tino.vn/ekyc/...`, `*.hitechcloud.vn/api/vneidekyc/ekyc/...`) are rewritten to the Zalo mini-app.

### Installation

1. Clone the plugin into your Hermes plugins directory:
   ```bash
   git clone https://github.com/hitechcloudvn/hermes-zalo-plugin.git ~/.hermes/plugins/hermes-zalo-plugin
   ```
2. Install the sidecar dependencies:
   ```bash
   cd ~/.hermes/plugins/hermes-zalo-plugin/sidecar
   npm ci || npm install
   ```
3. (Optional) Install extra Python packages: `google-api-python-client`, `google-auth` (Google Sheets); `Pillow` (image downscale).
4. Copy `.env.example` to `.env` (or declare the variables in your Hermes config) and fill them in.
5. Restart Hermes. On first run, scan the Zalo QR code (session is stored in `ZALO_PERSONAL_SESSION_DIR`).
6. Set `ZALO_PERSONAL_OWNER_UID` — only this UID has full control of the bot.

### Configuration

Environment variables (see also `.env.example`):

| Variable | Required | Default | Description |
|---|---|---|---|
| `ZALO_PERSONAL_OWNER_UID` | ✅ | — | Zalo UID of the account owner (bot operator). Only this user has full control. |
| `ZALO_PERSONAL_OWNER_USER_ID` | | = `OWNER_UID` | Hermes user_id used to map identity/memory. |
| `ZALO_PERSONAL_ALLOWED_USERS` | | — | Comma-separated Zalo UIDs also allowed to chat with the bot. |
| `ZALO_PERSONAL_SIDECAR_PORT` | | `3838` | Node.js sidecar port (127.0.0.1). |
| `ZALO_PERSONAL_PROXY` | | — | Proxy for the sidecar (`http://user:pass@host:port` or `socks5://...`). A residential proxy in the same country as the Zalo account is recommended. |
| `ZALO_PERSONAL_SESSION_DIR` | | `/opt/data/zalo` | Session + data directory. MUST be identical for the Node sidecar and the Python adapter. |
| `ZALO_PERSONAL_MAX_CONCURRENT_DOWNLOADS` | | `4` | Max concurrent media downloads in the sidecar. |
| `HITECHCLOUD_LANDING_BRIDGE_URL` | | `https://mcp.hitechcloud.vn/tools/landing_upload_image` | Server-to-server endpoint for Zalo → landing image upload. |
| `HITECHCLOUD_LANDING_BRIDGE_KEY` | | — | Dedicated key that may only call `landing_upload_image`. Read from env only — never logged, never sent to the model. |
| `ZALO_PERSONAL_GROUP_GREETING` | | `true` | Auto-greet the whole group when the bot joins (once per group). |
| `ZALO_PERSONAL_AUTO_FRIEND_ON_DM` | | `true` | Strangers DMing the bot get an automatic friend request (shares the `daily_friend_cap`). |
| `ZALO_PERSONAL_AUTO_FRIEND_MSG` | | `Mình kết bạn để tiện hỗ trợ nhé!` | Message attached to automatic friend requests. |
| `ZALO_PERSONAL_NAME_TRIGGERS` | | — | Comma-separated names that wake the bot in groups (e.g. `ông bụt,bụt`) — no @tag needed. |
| `ZALO_OWNER_NICKNAME` | | `sếp` | How the bot addresses the owner. |
| `ZALO_OWNER_NAME` | | — | Owner's real name to redact if the bot slips. Empty = no redaction. |
| `GOOGLE_TOKEN_PATH` | | — | Path to `google_token.json` (your Google OAuth) to enable Google Sheet export. |
| `ZALO_PERSONAL_HOME_THREAD` | | — | Default thread/chat ID for cron/notifications. |
| `ZALO_IMAGE_URL_ALLOWED_HOSTS` | | `mcp.hitechcloud.vn` | Allowed hosts when `zalo_send_image` fetches an `image_url` (comma-separated). SSRF guard. If overridden, include `mcp.hitechcloud.vn` yourself to keep QR sending working. |

### Tools

The bot registers 52 tools for the agent. Note: marketing/scan/friend tools must only be used for lawful purposes; daily caps exist to avoid account bans.

| Tool | Description |
|---|---|
| `zalo_groups_list` | List groups the bot has joined (group_id, member count, last activity, shared_session_id). |
| `zalo_set_chat_mode` | Owner-only: change the bot's behaviour mode for a specific chat. |
| `zalo_get_chat_mode` | Return the current mode + settings of a chat. |
| `zalo_set_digest` | Owner-only: toggle the daily 8 AM digest for a chat. |
| `zalo_set_persona` | Owner-only: update the bot's persona (name, self-intro, personality). |
| `zalo_get_persona` | Return the bot's current persona. |
| `zalo_reset_persona` | Owner-only: restore the default persona. |
| `zalo_set_chat_persona` | Owner-only: set a mission + style for one group/chat. |
| `zalo_get_chat_persona` | Owner-only: view a chat's own persona and its effective persona. |
| `zalo_group_summary` | Fetch a group's recent messages (shared session) for summaries / Q&A. |
| `zalo_react` | Drop a reaction on the latest message in the current chat. |
| `zalo_send_sticker` | Send a context-fitting sticker (keyword = emotion/meaning). |
| `zalo_set_reactions` | Owner-only: enable/disable reactions in a chat. |
| `zalo_add_keyword_alert` | Owner-only: subscribe to keyword alerts in a Zalo group. |
| `zalo_list_keyword_alerts` | List all keyword alert rules. |
| `zalo_remove_keyword_alert` | Owner-only: delete a keyword alert rule. |
| `zalo_toggle_keyword_alert` | Owner-only: enable/disable a keyword alert rule. |
| `zalo_list_products` | List the sales-mode product catalog (owner-only). |
| `zalo_add_product` | Add/upsert one product in the catalog (owner-only). |
| `zalo_update_product` | Partially update one product (owner-only). |
| `zalo_remove_product` | Remove one product from the catalog (owner-only). |
| `zalo_update_sales_rules` | Update sales-mode safety rules (cooldown, quota, avoid keywords). |
| `zalo_record_sales_pitch` | Record that a pitch was just sent — updates cooldown + daily quota. |
| `zalo_sales_quota` | Check a group's sales quota (can we pitch, why not). |
| `zalo_send_html` | Owner-only: build an HTML file from content and send it to the chat. |
| `zalo_send_pdf` | Render HTML → PDF (WeasyPrint) and send it (quotes, contracts, brochures). |
| `zalo_send_file` | Send an existing file (docx, zip, mp3…) from a public URL into the chat. |
| `zalo_send_pptx` | Build a PowerPoint from a slide spec and send it to the chat. |
| `zalo_send_xlsx` | Build an Excel workbook from a sheets/rows spec and send it. |
| `zalo_send_image` | Send an image to a customer — prefers internal `image_url`, fetched by the adapter (keeps the context small). |
| `zalo_escalate_to_owner` | DM the owner when stuck or a customer needs a human (rate-limited). |
| `zalo_friend_add` | Send a friend request to one person. |
| `zalo_friend_accept` | Accept a friend request from a uid. |
| `zalo_friend_sync` | Reconcile contacts — mark leads that accepted the friend request. |
| `zalo_send_dm` | DM one person directly, with multiple images if needed. |
| `zalo_scan_group` | Scan group members from a `zalo.me/g/...` link (no join needed; background scan spread over ~24 h). |
| `zalo_master_sheet` | Get the shared Google Sheet managing all leads + sync latest status. |
| `zalo_lookup_phones` | Map a list of phone numbers → Zalo accounts (uid, name) → leads + Sheet. |
| `zalo_marketing_prepare` | Prepare a friend/messaging batch within the daily caps — returns leads + briefs. |
| `zalo_marketing_send` | Send a prepared batch AFTER the owner approves (optional images). |
| `zalo_marketing_settings` | View/edit marketing caps, toggle auto-accept friend requests. |
| `zalo_campaign_report` | Marketing funnel report (scanned → invited → accepted → messaged). |
| `zalo_campaign_sync` | Sync the campaign's Google Sheet from the lead store. |
| `zalo_create_poll` | Create a poll in the current Zalo group. |
| `zalo_create_note` | Create a note on the group board (can pin). |
| `zalo_create_reminder` | Create a NATIVE Zalo reminder — only when the owner explicitly says "zalo". |
| `zalo_schedule_reminder` | Schedule a group reminder: the bot posts a message and @-tags the target when due. |
| `zalo_board_action` | Group board actions: list notes/polls/reminders, poll_vote, poll_lock, note_edit… |
| `zalo_read_recent_image` | Get the latest image a user sent in the current chat (last 5 kept per chat). |
| `zalo_upload_recent_image_to_landing` | Push the latest customer image to this conversation's demo landing, returns a public `image_url`. |
| `set_channel_active` | Owner-only: enable/disable one bot channel (e.g. `telegram-personal`). |
| `zalo_api_call` | Owner-only — power tool: call any zca-js method directly. |

### Owner commands (`/bot`)

Owner-only — send in the owner DM or in any group the bot is in:

| Command | Effect |
|---|---|
| `/bot status` | Show this chat's status (mode, daily_digest, chat_id). |
| `/bot mode <type>` | Change mode: `active` / `mention_only` / `listen_only` / `mute` / `default`. |
| `/bot modes` | List available modes. |
| `/bot digest <on\|off>` | Toggle the daily digest for this chat. |
| `/bot baotri` | Show maintenance mode status. |
| `/bot baotri <message+time>` | ENABLE maintenance with an auto-sent customer notice (e.g. `Bọn em bảo trì tới 15h30 hôm nay ạ`). |
| `/bot baotri on\|off` | Enable (default message) / disable maintenance mode. |
| `/bot help` | Show help. |

Chat modes:

| Mode | Behaviour |
|---|---|
| `active` | The bot replies to every message (no tag needed). |
| `mention_only` | Replies only when @mentioned or when replying to the bot (default). |
| `listen_only` | Reads + stores context, never replies. |
| `mute` | Ignores this chat entirely. |
| `default` | Follow the global config (`mention_only`). |

The owner can also just say things naturally ("em theo dõi group này tích cực" / "stop replying in here") — the bot switches modes accordingly.

### Reminders

* **Group reminders** (`zalo_schedule_reminder`): multiple fire times (`fire_times`); when due, the bot posts a reminder and @-tags the target. Escalates per attempt (softer first, firmer later).
* **Native reminders** (`zalo_create_reminder`): creates a reminder on the Zalo board — only when the owner explicitly says "zalo".
* **Reminder composition** (`reminder_compose.py`): a toolless LLM (no agent, no tools) writes the Vietnamese reminder; on error/empty it falls back to a template. The reminder body is treated as USER DATA (injection-safe), and `@All` / owner-name mentions have their `@` stripped before send.

### Media pipeline

* **Inbound media**: the sidecar streams downloads under the `media-contract.js` contract (size caps, magic-byte sniffing — file extensions are never trusted); cached at `<session_dir>/media-cache/` with content-addressed names (`<stem>-<sha256[:12]>.<ext>`).
* **Image sending** (`zalo_send_image` + `image_url_fetch.py` + `image_resize.py`): fetches images only from `ZALO_IMAGE_URL_ALLOWED_HOSTS` (SSRF guard), validates magic bytes, and downscales the longest side to 1024 (default) when Pillow is available.
* **Landing bridge** (`landing_media_bridge.py`): customer images are pushed to the conversation's demo landing **server-to-server** via `HITECHCLOUD_LANDING_BRIDGE_URL` + a dedicated key — base64 never travels through the LLM. Cache reads are fail-closed: path escapes, symlinks, non-image files, and oversize files are all rejected.
* **eKYC rewrite**: legacy eKYC links in outgoing text are rewritten to the Zalo mini-app (the token in the path is preserved).

### Tests

```bash
# Python (pytest)
python -m pytest -q

# Sidecar Node.js (node:test)
cd sidecar && npm ci || npm install && node --test
```

### License & Disclaimer

MIT — see [LICENSE](LICENSE). © 2026 HiTechCloud.VN.

This software is provided "AS IS" without warranty of any kind. Using unofficial Zalo APIs carries a risk of account limitation or suspension. The authors are not responsible for any damages, account restrictions, legal issues, or losses resulting from the use of this software. Always comply with Zalo's Terms of Service and applicable law.
