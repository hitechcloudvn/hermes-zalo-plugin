"""Plugin Zalo cá nhân cho Hermes Agent — điểm vào ``register``.

Khi Hermes nạp plugin dưới dạng package, ``register`` đến từ ``adapter``.
Khi trình chạy test (pytest) nạp file này như một module trần (không có
package cha), ta không đụng tới adapter (adapter cần Hermes gateway) — chỉ
khai báo ``register = None`` để việc import không nổ.

----

Personal-Zalo plugin for Hermes Agent — the ``register`` entry point.

When Hermes loads the plugin as a package, ``register`` comes from ``adapter``.
When a test runner (pytest) imports this file as a bare top-level module (no
parent package), the adapter (which needs the Hermes gateway) is NOT touched —
``register = None`` is declared instead so the import does not blow up.
"""
if __package__:
    from .adapter import register
else:  # test-runner context (pytest Package.setup) — no Hermes gateway here
    register = None  # type: ignore[assignment]
