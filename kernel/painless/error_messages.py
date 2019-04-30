class Messages:
    required = 'لطفا این فیلد را پر نمایید'
    email_validation = 'لطفا ایمیل را به درستی وارد نمایید'
    
    def max_length(self, number):
        return 'این فیلد نمی تواند بیش از {} کاراکتر باشد'.format(number)