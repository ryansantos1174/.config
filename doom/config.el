(setq user-full-name "Ryan De Los Santos"
      user-mail-address "ryansantos1174@gmail.com")

(setq doom-theme 'doom-monokai-pro)
(setq doom-font "SauceCodePro Nerd Font-14")
(setq display-line-numbers-type 'relative)

(use-package! olivetti
  :ensure t)
(olivetti-mode t)

(add-to-list 'exec-path "~/.cargo/bin")
(add-to-list 'exec-path "/usr/bin/fish")

(smartparens-mode 0);

;; (use-package exwm
;;   :config
;;   (setq exwm-workspace-number 5)
;;   (exwm-enable))

  ;; Change faces

(setq org-agenda-files '(
                         "~/Documents/ToDo/gtd.org"
                         "~/Dropbox/org/ToDo/tickler.org"
                         ))

(after! org
  (setq org-capture-templates
        '(("p" "Project" entry
           (file+headline "~/Documents/ToDo/inbox.org" "Tasks")
                "*TODO %i%?"
                :kill-buffer t)
          ("t" "Todo [inbox]" entry
           (file+headline "~/Documents/ToDo/inbox.org" "Tasks")
                          "* TODO %i%?"
                          :kill-buffer t)
           ("T" "Tickler" entry
            (file+headline "~/Documents/ToDo/tickler.org" "Tickler")
            "* %i%? \n %U"
            :kill-buffer t))))

(setq org-refile-targets '(("/home/ryan/Documents/ToDo/gtd.org" :maxlevel . 3)
                          ("/home/ryan/Documents/ToDo/tickler.org" :maxlevel . 3)
                          ("/home/ryan/Documents/ToDo/someday.org" :maxlevel . 3)))

;;(require 'org-bullets)(add-hook 'org-mode-hook (lambda () (org-bullets-mode 1)))
(setq org-agenda-span 7)
(setq org-refile-history nil)
(add-hook 'org-mode-hook (lambda ()
                           (set (make-local-variable 'display-line-numbers) nil)
                            ))


(use-package org-modern
  :hook (org-mode . org-modern-mode)
  :config
  (setq org-modern-star '("◉" "○" "◈" "◇" "✳" "◆" "✸" "▶")
        org-modern-table-vertical 2
        org-modern-table-horizontal 4
        org-modern-list '((45 . "➤") (43 . "–") (42 . "•"))
        org-modern-priority t
        org-modern-block t
        org-modern-block-fringe nil
        org-modern-horizontal-rule t
        org-modern-todo-faces (quote '(("TODO" :background "red" :foreground "black")("STRT" :background "yellow" :foreground "black")("DONE" :background "green" :foreground "black")("CANCELLED" :background "grey" :foreground "black")))
        ))


(setq org-hide-emphasis-markers t
      org-fontify-done-headline t
      org-hide-leading-stars t
      org-pretty-entities t
      org-odd-levels-only t)

(org-babel-do-load-languages
 'org-babel-load-languages
 '((shell . t)))

(setq calendar-week-start-day 1)

(setq org-pomodoro-finished-sound "~/.doom.d/extra/sounds/pomodoroBell.wav")
(setq org-pomodoro-short-break-sound "~/.doom.d/extra/sounds/pomodoroBell.wav")
(setq org-pomodoro-long-break-sound "~/.doom.d/extra/sounds/pomodoroBell.wav")
(setq org-pomodoro-audio-player "aplay")
(setq org-pomodoro-tick-hook t)
(setq org-pomodoro-finished-hook t)
(setq org-pomodoro-started-hook t)
(setq org-pomodoro-length 35)
(setq org-pomodoro-short-break-length 5)
(setq org-pomodoro-long-break-length 30)
(setq org-pomodoro-ticking-sound-p nil)

(add-hook 'org-pomodoro-started-hook
          (lambda ()
            (setq org-pomodoro-ticking-sound-p nil)))

(add-hook 'org-pomodoro-tick-hook
          (lambda ()
             (when (equal(floor (org-pomodoro-remaining-seconds)) 10)
                (setq org-pomodoro-ticking-sound-p t))))

(add-hook 'org-pomodoro-finished-hook
          (lambda ()
            (setq org-pomodoro-ticking-sound-p nil)))

(defun pass-push ()
  "Pushes to git repo to update password store"
  (interactive)
  (shell-command
   "pass git push -u --all&"
   ))

(setq counsel-spotify-client-id "ddfcbccc90d548efb5e0f9398825b1c9")
(setq counsel-spotify-client-secret "52c0236c71434f55a917d695db6d08b4")
(setq counsel-spotify-service-name "spotify")

(use-package lsp-mode
  :ensure
  :commands lsp
  :custom
  ;; what to use when checking on-save. "check" is default, I prefer clippy
  (lsp-rust-analyzer-cargo-watch-command "clippy")
  (lsp-eldoc-render-all t)
  (lsp-idle-delay 0.6)
  ;; enable / disable the hints as you prefer:
  (lsp-rust-analyzer-server-display-inlay-hints t)
  (lsp-rust-analyzer-display-lifetime-elision-hints-enable "skip_trivial")
  (lsp-rust-analyzer-display-chaining-hints t)
  (lsp-rust-analyzer-display-lifetime-elision-hints-use-parameter-names nil)
  (lsp-rust-analyzer-display-closure-return-type-hints t)
  (lsp-rust-analyzer-display-parameter-hints nil)
  (lsp-rust-analyzer-display-reborrow-hints nil)
  :config
  (add-hook 'lsp-mode-hook 'lsp-ui-mode))

(use-package lsp-ui
  :ensure
  :commands lsp-ui-mode
  :custom
  (lsp-ui-peek-always-show t)
  (lsp-ui-sideline-show-hover t)
  (lsp-ui-doc-enable nil))

(use-package rustic
  :ensure
  :bind (:map rustic-mode-map
              ("M-j" . lsp-ui-imenu)
              ("M-?" . lsp-find-references)
              )
:config
(setq rustic-format-on-save t)
)

;; (use-package eaf
;;   :load-path "~/.emacs.d/site-lisp/emacs-application-framework"
;;   :custom
;;   ; See https://github.com/emacs-eaf/emacs-application-framework/wiki/Customization
;;   (eaf-browser-continue-where-left-off t)
;;   (eaf-browser-enable-adblocker t)
;;   (browse-url-browser-function 'eaf-open-browser)
;;   :config
;;   (defalias 'browse-web #'eaf-open-browser))
;; (require 'eaf-browser)
;; (require 'eaf-evil)

(map! :leader
      :desc "Open Terminal"
      "v" #'vterm)
(map! :leader
      :desc "Delete"
      "x" #'delete-backward-char)
