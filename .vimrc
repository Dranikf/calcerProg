set number
set tabstop=4

set hlsearch
let g:mapleader = ','

" настройка плагинов для vim-plug
call plug#begin('~/.vim/plugged')
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'ycm-core/YouCompleteMe'
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
Plug 'kien/ctrlp.vim'
Plug 'easymotion/vim-easymotion'
call plug#end()

"mappings
map <C-n> :NERDTreeToggle<CR>
map <Leader> <Plug> (easymotion-prefix)
"mappings

" мой конфиг на vim

