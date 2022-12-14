(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(org-agenda-files
   '("/home/ryan/Documents/ToDo/tickler.org" "/home/ryan/Documents/ToDo/gtd.org"))
 '(org-todo-keyword-faces
   '(("[-]" . +org-todo-active)
     ("STRT" . "yellow")
     ("[?]" . +org-todo-onhold)
     ("WAIT" . +org-todo-onhold)
     ("HOLD" . +org-todo-onhold)
     ("PROJ" . +org-todo-project)
     ("NO" . +org-todo-cancel)
     ("KILL" . +org-todo-cancel)))
 '(package-selected-packages
   '(org-journal evil-mc olivetti elpy pdf-tools org-modern lsp-ui flycheck exwm exec-path-from-shell blacken)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(org-modern-statistics ((t (:inherit org-checkbox-statistics-todo))))
 '(org-modern-tag ((t (:inherit (region org-modern-label))))))
