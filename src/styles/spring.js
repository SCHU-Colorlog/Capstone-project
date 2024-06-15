import styled from 'styled-components';
import { createGlobalStyle } from 'styled-components';

export const Wrapper = styled.div`
    background-color: rgba(240, 180, 179, 0.3);
    width: 40vw;
    margin: 0 auto;
    align-items: center;
    display: flex;
    flex-direction: column;
    font-family: 'Pretendard-Regular'
`;

export const Header = styled.div`
    text-align: center;
    justify-content: center;
    align-items: center;
    width: 40vw;

`;

export const Infobox = styled.div`
    height: 110px;
    color: #545454;
    width: 40vw;
    background-color: #FFF6F6;
    box-shadow: 0px 6px 10px rgba(135, 135, 135, 0.25);
    font-weight: 500px;
    font-size: 18px;
    font: #000000;
    margin: 0;
    display: grid;
    place-items: center; /* 수평 및 수직 가운데 정렬 */ /* 컨테이너 높이 설정 (원하는 높이로 조절) */
    position: relative; /* 위치 지정 */
    z-index: 1;
`

export const Buttonzone = styled.div`
    height: 110px;
    display: flex;
    justify-content: space-evenly;
    align-items: center;

    & > button {
        border-radius: 10px;
        height: 59px;
        width: 175px;
        background-color: #ffffff;
        box-shadow: 0px 8px 20px rgba(148, 148, 148, 0.25);
        font-size: 18px;
        font-weight: 450;
        font: black;
        border: none;
        cursor: pointer;

        &:hover {
        content: "";
        transform: scale(1.1, 1.1);
        -ms-transform: scale(1.1, 1.1);
        -webkit-transform: scale(1.1, 1.1);
        box-shadow: 0px 5px 5px -2px rgba(0, 0, 0, 0.25);
    }
    }

`;

export const GlobalStyle = createGlobalStyle`
    @font-face {
        font-family: 'SF_HambakSnow';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2106@1.1/SF_HambakSnow.woff') format('woff');
        font-weight: normal;
        font-style: normal;
    }
    @font-face {
        font-family: 'SokchoBadaDotum';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2402_1@1.0/SokchoBadaDotum.woff2') format('woff2');
        font-weight: normal;
        font-style: normal;
    }
    @font-face {
        font-family: 'Pretendard-Regular';
        src: url('https://cdn.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
        font-weight: 400;
        font-style: normal;
    }
`;

export const Logo = styled.div`
    box-shadow: 0px 6px 10px rgba(113, 113, 113, 0.25);
    height: 130px;
    display: flex;
    align-items: center;
    flex-direction: column;
    font: #4f4f4f;
    position: relative; /* 위치 지정 */
    z-index: 2;
    font-family: 'SF_HambakSnow';

    & > h1 {
        font-size: 60px;
    }
`;

export const MainContainer = styled.div`
    background-color: #ffffff;
    box-shadow: 0px 8px 20px rgba(148, 148, 148, 0.25);
    font: #4f4f4f;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-direction: column;
    width: 35vw;  
`;

export const Contents = styled.div`
    flex: 1;
    margin: 5px 10px; /* 상단과 하단 간격 설정 */
    text-align: center; /* 텍스트 가운데 정렬 */ /* 테두리 스타일 설정 */
    padding: 15px;

    & > p {
        font-size: 25px;
    }

    & > h1 {
        font-size: 40px;
        color: #494949;
    }
`;

export const Contents2 = styled.div`
    flex: 1; /* 상단과 하단 간격 설정 */
    text-align: center; /* 텍스트 가운데 정렬 */ /* 테두리 스타일 설정 */
    padding: 5px; /* 내부 여백 설정 */

    & > h1 {
        font-size: 50px;
        font-family: 'SF_HambakSnow'
    }

    & > h3 {
        font-size: 23px;
    }
`;

export const Contents3 = styled.div`
  flex: 1;
  margin: 5px 10px; /* 상단과 하단 간격 설정 */
  padding: 15px;
  display: flex;
  flex-direction: column; /* 자식 요소를 세로로 배치 */
`

export const ImageText1 = styled.div`
    display: flex;
    align-items: center;

    & > div {
        margin: 20px;
    }

    & > div > h2 {
        color: #494949;
        font-size: 27px;
    }
`

export const Fimg = styled.img`
    width: 233px; /* 이미지 컨테이너의 너비 */
    height: 287px;
`

export const Cimg = styled.img`
    max-width: 270px;
`

export const Margin1 = styled.div`

    & > img {
        max-width: 170px; /* 이미지의 최대 너비 설정 */
        margin-right: 50px;
    }

    & > h3 {
        font-size: 20px;
    }
`

export const ImageText2 = styled.div`
    max-width: 170px; /* 이미지의 최대 너비 설정 */
    display: flex; /* 수평 중앙 정렬을 위해 플렉스 박스 사용 */
    justify-content: center; /* 수평 가운데 정렬 */
    align-items: center; /* 수직 가운데 정렬 */
    margin: 20px 0;
    
    & > img {
        padding: 0; /* 패딩 설정 제거 (선택 사항) */
        border: 0; /* 이미지 테두리 제거 (선택 사항) */
    }
`

export const ImageText3 = styled.div`
  max-width: 100%; /* 부모 요소의 최대 너비로 설정 */
  display: flex; /* 수평 중앙 정렬을 위해 플렉스 박스 사용 */
  justify-content: space-between; /* 요소를 여백 너비 일정하게 양끝과 가운데에 배치 */
  margin: 20px 0; /* 위아래 여백 설정 */

  & > img {
    padding: 0; /* 패딩 설정 제거 (선택 사항) */
    border: 0; /* 이미지 테두리 제거 (선택 사항) */
    width: 165px;
    height: 195px;
  }
`

export const Margin2 = styled.div`
    margin: 50px;
`

export const Sub = styled.div`
    display: flex;
    flex-direction: column;
    width: 35vw;
    border: 3px solid #494949;
`

export const SubContainer1 = styled.div`
    height: 50px;
    border-bottom: 1px solid rgb(0, 0, 0);
    display: flex;
    justify-content: space-between;
    padding: 0 10px;
    margin: 0 10px;
    box-sizing: border-box;

    & > p {
        font-size: 20px;
        font-weight: 500;
        align-items: center;
        display: flex;
        color: #4B4B4B;
        font-family: 'SF_HambakSnow'
    }

    & > h3 {
        font-size: 20px;
        align-items: center;
        display: flex;
        color: #4B4B4B;
    }
`

export const SubContainer2 = styled.div`
    height: 300px; 
    box-sizing: border-box;
    justify-content: center;
    display: flex;
    margin: 0 10px;
`

export const SubContainer3 = styled.div`
    height: 180px; 
    border-top: 1px solid rgb(0, 0, 0);
    box-sizing: border-box;
    justify-content: center;
    display: flex;
    margin: 0 10px;
`

export const LowText = styled.div`
    font-size: 20px;
    font-weight: 200;
    font-family: Georgia, 'Times New Roman', Times, serif;
`

export const Rimage1 = styled.img`
    border-radius: 50%; /* 50%로 설정하여 이미지를 원 모양으로 만듭니다. */
    width: 240px; /* 원 모양의 크기를 조절합니다. 필요에 따라 조절하세요. */
    height: 240px;
    border: 1px solid #4b4b4b;
    margin-right: 10px;
`

export const Rimage2 = styled.img`
    border-radius: 50%; /* 50%로 설정하여 이미지를 원 모양으로 만듭니다. */
    width: 130px; /* 원 모양의 크기를 조절합니다. 필요에 따라 조절하세요. */
    height: 130px;
    border: 1px solid #4b4b4b;
`

// export const Input2 = styled.textarea`
//     margin: 20px;
//     width: 93%;
//     height: 40vh;
//     resize: none;
//     display: flex;
//     justify-content: space-between;
//     padding: 10px 13px;
//     font-size: 18px;
//     font-family: monospace;
//     font-weight: 600;
//     white-space: pre; /* 공백 문자(들여쓰기)를 유지하도록 설정 */
//     tab-size: 3; /* 탭 문자 크기를 지정 (들여쓰기 간격) */
//     background-color: #f2f2f2;
//     border: 0;
//     border-radius: 10px;
//     &:focus{
//             outline: none;
//         }
// `;

// export const Button = styled.button`
//     display: flex;
//     width: 200px;
//     height: 50px;
//     margin: 0 auto;
//     align-items: center;
//     justify-content: center;
//     border-radius: 40px;
//     border: none;
//     font-size: 20px;
//     font-weight: 500;
//     cursor: pointer;
//     background-color: #26539C;
//     color: #ffffff;
//     position: relative;
//     transition: transform 0.3s;

//     &:hover {
//         content: "";
//         transform: scale(1.1, 1.1);
//         -ms-transform: scale(1.1, 1.1);
//         -webkit-transform: scale(1.1, 1.1);
//         box-shadow: 0px 5px 5px -2px rgba(0, 0, 0, 0.25);
//     }
// `;
