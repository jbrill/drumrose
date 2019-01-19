<template>
  <div class="unloggedContain">
    <div class="unlogged--contain__upper-area">
      <nuxt-link to="/auth/sign-in">
        <button class="unlogged-contain__upper--area__sign--up">Sign up</button>
      </nuxt-link>
      <p class="unlogged-contain__upper--area__log-in__text">
        Already a member?
      </p>
      <nuxt-link to="/auth/sign-in">
        <a class="unlogged-contain__upper--area__log-in__btn">Sign in</a>
      </nuxt-link>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.unloggedContain {
  background-color: var(--primary-red);
}
.unlogged--contain__upper--area__description {
  position: absolute;
  color: white;
  top: 0;
  margin: 0 auto;
  text-align: center;
  font-weight: 100;
  font-size: 1rem;
  margin-top: 24rem;
}
.unlogged-contain__upper--area__sign--up {
  position: absolute;
  color: white;
  background-color: #772ce6;
  top: 0;
  border: none;
  width: 8rem;
  height: 3rem;
  border-radius: 2px;
  text-align: center;
  font-weight: 100;
  font-size: 1rem;
  box-shadow: 0px 13px 21px -10px rgba(0, 0, 0, 0.3);
}
.unlogged-contain__upper--area__log-in__text {
  position: absolute;
  color: black;
  top: 0;
  text-align: center;
  font-weight: 100;
  font-size: 0.8rem;
}
.unlogged-contain__upper--area__log-in__btn {
  position: absolute;
  color: #c0102c;
  top: 0;
  text-align: center;
  font-weight: bolder;
  font-size: 0.8rem;
}
.unlogged--contain__upper-area {
  max-height: 35rem;
  overflow: hidden;
}
</style>
